from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop_subscription_plan, name='shop_subscription_plan'),
    path('<int:plan_id>/', views.get_plan_id, name='get_plan_id'),
    path('add_plan_admin/', views.add_plan_admin, name='add_plan_admin'),
    path('edit_plan_admin/<int:plan_id>', views.edit_plan_admin, name='edit_plan_admin'),
    path('checkout_plan/', views.checkout_plan, name='checkout_plan'),
    path('thanks/', views.thanks, name='thanks'),
    path('stripe_webhook/', views.stripe_webhook, name='stripe_webhook')   
]