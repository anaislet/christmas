from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from . import forms
from .models import Family, Member
from django.views.generic import View

def identification_page(request):
    login_form = forms.CustomLoginForm()
    registration_form = forms.CustomRegistrationForm()
    message = ''

    if request.method == 'POST':
        login_form = forms.CustomLoginForm(request.POST)
        registration_form = forms.CustomRegistrationForm(request.POST)

        if login_form.is_valid():

            member_name_form = login_form.cleaned_data.get('member_name')
            password_form = login_form.cleaned_data.get('family_password')

            try:
                member_model = Member.objects.get(name__iexact= member_name_form)
                family_model = Family.objects.get(name=member_model.family)

                if family_model.password != password_form:
                    message = "Ce mot de passe ne correspond à aucune famille enregistrée"

                else:
                    request.session['member'] = member_name_form
                    return redirect("home", member_model.id)

            except Member.DoesNotExist:

                try:
                    new_member_family = Family.objects.get(password=password_form)
                    new_member = Member.objects.create(name=member_name_form, family=new_member_family)
                    request.session['member'] = new_member.name
                    return redirect("home", new_member.id)
                
                except Family.DoesNotExist:
                    message = "Ce mot de passe ne correspond à aucune famille enregistrée"

        elif registration_form.is_valid():

            family_name_form = registration_form.cleaned_data.get('family_name')
            password_form = registration_form.cleaned_data.get('family_password')

            try:
                new_family = Family.objects.create(name=family_name_form, password=password_form)
                message="Votre famille a été correctement ajoutée, créé vous en tant que member maintenant"
            
            except Family.DoesNotExist:
                message="La saisie est incorrecte"

    return render(request, 'identification.html', context={'login_form': login_form, 'registration_form': registration_form, 'message': message})
