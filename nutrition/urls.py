from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_nutrition_plan, name='shop_nutrition_plan'),
    path('add_nutrition_plan/', views.add_nutrition_plan_admin, name='add_nutrition_plan_admin'),
]