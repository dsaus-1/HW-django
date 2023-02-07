from django import forms
from catalog.models import Product, Version


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['user', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_product_name(self):
        product = self.cleaned_data['product_name']
        stop_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', 'алкоголь', 'сигареты', 'табак']

        for word in stop_word:
            if word in product:
                raise forms.ValidationError('Данный продукт противоречит политике магазина')

        return product

    def clean_descriptions(self):
        descriptions = self.cleaned_data['descriptions']
        stop_word = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар', 'алкоголь', 'сигареты', 'табак']

        for word in stop_word:
            if word in descriptions:
                raise forms.ValidationError('Данный продукт противоречит политике магазина')

        return descriptions

class ModeratorProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('descriptions', 'status', 'category',)


class VersionForm(forms.ModelForm):

    class Meta:
        model = Version
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'