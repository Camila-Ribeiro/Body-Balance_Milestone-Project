from django import forms
from .models import Plan


class AddPlanForm(forms.ModelForm):

    class Meta:
        model = Plan
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        plan = Plan.objects.all()
