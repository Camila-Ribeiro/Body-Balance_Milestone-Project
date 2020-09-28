from django.urls import path
from . import views

urlpatterns = [
    path('', views.profile, name='profile'),
    path('product_order_history/<order_number>', views.product_order_history, name='product_order_history'),
    path('subscription_order_history/<order_number>', views.subscription_order_history, name='subscription_order_history'),
    path('nutrition', views.nutrition, name='nutrition'),
]