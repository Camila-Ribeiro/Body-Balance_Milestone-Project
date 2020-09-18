from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_nutrition_plan, name='shop_nutrition_plan'),
]