from django import forms
from .models import Card
from decimal import Decimal


class CardForm(forms.Form):
    class Meta:
        model = Card
        fields = '__all__'

    card_image = forms.FileField(
        label='Ảnh card', required=False,
        widget=forms.FileInput(
            attrs={
                'type': 'file',
                'class': 'd-none',
                'accept': 'image/*',
                'multiple': True
            }
        )
    )

    card_name = forms.CharField(
        label='Tên card', min_length=3, max_length=300, required=False,
        help_text='Tên card',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-range',
                'placeholder': 'Tên card'
            }
        )
    )

    card_price = forms.DecimalField(
        label='Giá card', max_digits=10, decimal_places=2, required=False,
        help_text='Giá card',
        widget=forms.TextInput(
            attrs={
                'class': 'form-control form-control-range',
                'placeholder': '0.00',
                'autofocus': 'true',
            }
        )
    )


