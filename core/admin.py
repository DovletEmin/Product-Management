from django.contrib import admin
from .models import Category, Tag, Product, ProductImage

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'category', 'is_published', 'owner', 'created_at')
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ProductImageInline]

admin.site.register(Category)
admin.site.register(Tag)
