from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_all_products, name='shop_products'),
    path('<int:product_id>/', views.get_product_detail, name='get_product_detail'),
    path('add_admin/', views.add_product_to_admin, name='add_product_to_admin'),
]