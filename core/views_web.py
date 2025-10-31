from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Product
from .forms import ProductForm, ProductImageForm
from django.db.models import Sum, F


def product_list(request):
    products = Product.objects.select_related('category').prefetch_related('tags', 'images')
    
    total_stock = products.aggregate(total=Sum('stock'))['total'] or 0
    total_value = products.aggregate(total=Sum(F('stock') * F('price')))['total'] or 0

    context = {
        'products': products,
        'total_stock': total_stock,
        'total_value': total_value,
    }
    return render(request, 'products/product_list.html', context)

def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'products/product_detail.html', {'product': product})

@login_required
def product_create(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        image_form = ProductImageForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.owner = request.user
            product.save()
            form.save_m2m()
            if image_form.is_valid() and image_form.cleaned_data.get('image'):
                img = image_form.save(commit=False)
                img.product = product
                img.save()
            messages.success(request, 'Продукт успешно добавлен!')
            return redirect('products:web_list')
    else:
        form = ProductForm()
        image_form = ProductImageForm()
    return render(request, 'products/product_form.html', {'form': form, 'image_form': image_form})

@login_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk, owner=request.user)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Продукт обновлён!')
            return redirect('products:web_detail', pk=pk)
    else:
        form = ProductForm(instance=product)
    return render(request, 'products/product_form.html', {'form': form, 'product': product})
