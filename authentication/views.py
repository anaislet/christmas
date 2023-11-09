from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from . import forms
from .models import Family, Member
from django.views.generic import View

def login_page(request):
    form = forms.CustomLoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.CustomLoginForm(request.POST)
        if form.is_valid():

            member_name_form = form.cleaned_data.get('member_name')
            password_form = form.cleaned_data.get('family_password')

            member_model = Member.objects.get(name= member_name_form)
            family_model = Family.objects.get(name=member_model.family)

            if family_model.password != password_form:
                message = "Ce mot de passe ne correspond à aucune famille enregistrée"

            else:
                request.session['member'] = member_name_form
                return redirect("home")

    return render(request, 'login.html', context={'form': form, 'message': message})
