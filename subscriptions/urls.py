from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_subscription_plan, name='shop_subscription_plan'),
    path('add_plan_admin/', views.add_plan_admin, name='add_plan_admin'),
]