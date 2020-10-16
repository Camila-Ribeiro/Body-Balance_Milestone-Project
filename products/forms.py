from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category


class AddProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image_file = forms.ImageField(label='Image File', required=False,
                                  widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        product_friendly_names = [(cat.id, cat.get_category_friendly_name())
                                  for cat in categories]

        self.fields['category'].choices = product_friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
