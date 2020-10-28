from django.urls import path
from . import views

urlpatterns = [
    path('', views.nutrition, name='nutrition'),
    path('<int:nutrition_id>/', views.get_nutrition_id,
         name='get_nutrition_id'),
    path('edit_menu_admin/<int:nutrition_id>', views.edit_menu_admin,
         name='edit_menu_admin'),
]
