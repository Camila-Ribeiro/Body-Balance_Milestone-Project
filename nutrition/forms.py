from django import forms
from .models import Nutrition


class AddNutritionPlanForm(forms.ModelForm):

    class Meta:
        model = Nutrition
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # nutrition_form = Nutrition.objects.all()
