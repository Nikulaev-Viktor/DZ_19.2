from django import forms
from django.core.exceptions import ValidationError
from django.forms import BooleanField

from catalog.models import Product, Version


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


class ProductForm(StyleFormMixin, forms.ModelForm):
    """Форма создания продукта"""

    class Meta:
        model = Product
        exclude = ('author', 'views_count')

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


class VersionForm(StyleFormMixin, forms.ModelForm):
    """Форма создания версии продукта"""

    class Meta:
        model = Version
        fields = '__all__'


class ProductModeratorForm(StyleFormMixin, forms.ModelForm):
    """Форма для модератора"""

    class Meta:
        model = Product
        fields = ("description", "category", "is_published",)
