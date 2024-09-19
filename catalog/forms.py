from django import forms
from django.core.exceptions import ValidationError

from catalog.models import Product, Version


class ProductForm(forms.ModelForm):
    """Форма создания продукта"""

    class Meta:
        model = Product
        fields = '__all__'

    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция',
                       'радар']
    def clean_title(self):
        """Валидация на запрещенные слова в названии"""
        cleaned_data = self.cleaned_data['title']
        for word in self.forbidden_words:
            if word in cleaned_data:
                raise ValidationError(f'Название продукта не должно содержать запрещенное слово: {word}')
        return cleaned_data

    def clean_description(self):
        """Валидация на запрещенные слова в описании"""
        cleaned_data = self.cleaned_data['description']
        for word in self.forbidden_words:
            if word in cleaned_data:
                raise ValidationError(f'Описание продукта не должно содержать запрещенное слово: {word}')
        return cleaned_data


class VersionForm(forms.ModelForm):
    model = Version
    field = '__all__'

