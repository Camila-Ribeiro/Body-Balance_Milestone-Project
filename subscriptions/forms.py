from django import forms
from .models import Plan
from checkout.models import SubscriptionOrder


class AddPlanForm(forms.ModelForm):

    class Meta:
        model = Plan
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        plan = Plan.objects.all()


class SubscriptionOrderForm(forms.ModelForm):
    class Meta:
        model = SubscriptionOrder
        fields = ('full_name', 'email', 'user_profile',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # plan = Plan.objects.all()
