from rest_framework import viewsets, permissions
from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer
from rest_framework.parsers import MultiPartParser, FormParser

class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.is_staff

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.select_related('category','owner').prefetch_related('tags','images').all()
    serializer_class = ProductSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
    parser_classes = [MultiPartParser, FormParser]
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
