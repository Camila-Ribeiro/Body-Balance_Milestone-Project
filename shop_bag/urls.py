from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_bag, name='shop_bag'),
    path('add/<product_id>', views.add_products_to_bag, name='add_products_to_bag'),
    path('update_quantity/<product_id>', views.update_quantity_bag, name='update_quantity_bag'),
    path('remove_product/<product_id>', views.remove_product, name='remove_product'),
]