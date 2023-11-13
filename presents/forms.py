from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Gift
from django.db import models

class ModifyGiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['name', 'link', 'price']
