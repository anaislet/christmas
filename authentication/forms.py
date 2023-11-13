from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Family, Member

class CustomLoginForm(forms.Form):
    member_name = forms.CharField(max_length=50, label='Nom d\'utilisateur')
    family_password = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Mot de passe')

class CustomRegistrationForm(forms.Form):
    family_name = forms.CharField(max_length=50, label='Nom de la famille')
    family_password = forms.CharField(max_length=50, widget=forms.PasswordInput, label='Mot de passe')
