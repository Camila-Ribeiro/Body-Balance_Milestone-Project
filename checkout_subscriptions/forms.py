from django import forms
from .models import SubscriptionOrder

class SubscriptionOrderForm(forms.ModelForm):
    class Meta:
        model = SubscriptionOrder
        fields = ('full_name',)

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, remove auto-generated
        labels and set autofocus on first field
        """
        super().__init__(*args, **kwargs)
        placeholders = {
            'full_name': 'Full Name',
        }
