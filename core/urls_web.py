from django.urls import path
from . import views_web

app_name = 'products'

urlpatterns = [
    path('', views_web.product_list, name='web_list'),
    path('create/', views_web.product_create, name='web_create'),
    path('<int:pk>/', views_web.product_detail, name='web_detail'),
    path('<int:pk>/edit/', views_web.product_edit, name='web_edit'),
]
