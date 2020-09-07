from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_bag, name='shop_bag'),
    path('add/<product_id>', views.add_products_to_bag, name='add_items_to_bag'),
]