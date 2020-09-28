from django.urls import path
from . import views

urlpatterns = [
    path('', views.nutrition, name='nutrition'),
    path('add_nutrition_plan/', views.add_nutrition_plan_admin, name='add_nutrition_plan_admin'),
]

