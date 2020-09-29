from django.urls import path
from . import views

urlpatterns = [
    path('', views.nutrition, name='nutrition'),
    path('add_menu_admin/', views.add_menu_admin, name='add_menu_admin'),
]

