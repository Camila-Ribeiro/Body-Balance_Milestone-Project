from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_all_products, name='shop_products'),
]
