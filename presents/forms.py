from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Gift
from django.db import models

class ModifyGiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['name', 'link', 'price']

        labels = {
            'name': 'Intitulé',
            'link': 'Lien URL',
            'price': 'Prix',
        }

        widgets = {
            'price': forms.Select(choices=Gift.Price.choices),
        }

class AddGiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['name', 'link', 'price']
        exclude = ['member', 'family']

        labels = {
            'name': 'Intitulé',
            'link': 'Lien URL',
            'price': 'Prix',
        }

        widgets = {
            'price': forms.Select(choices=Gift.Price.choices),
        }