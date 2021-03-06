from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_subscription_plan, name='shop_subscription_plan'),
    path('<int:plan_id>/', views.get_plan_id, name='get_plan_id'),
    path('edit_subscription_admin/<int:plan_id>',
         views.edit_subscription_admin, name='edit_subscription_admin'),
]
