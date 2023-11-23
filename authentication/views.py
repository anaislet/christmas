from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from . import forms
from .models import Family, Member
from django.views.generic import View

def identification_page(request):
    request.session['member'] = None
    request.session['member_id'] = None
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
                    request.session['member_id'] = member_model.id
                    return redirect("home", member_model.id)

            except Member.DoesNotExist:

                try:
                    new_member_family = Family.objects.get(password=password_form)
                    new_member = Member.objects.create(name=member_name_form, family=new_member_family)
                    request.session['member'] = new_member.name
                    request.session['member_id'] = new_member.id
                    return redirect("home", new_member.id)
                
                except Family.DoesNotExist:
                    message = "Ce mot de passe ne correspond à aucune famille enregistrée"

            login_form.errors.clear()

        elif registration_form.is_valid():

            family_name_form = registration_form.cleaned_data.get('family_name')
            password_form = registration_form.cleaned_data.get('family_password')
            password_form2 = registration_form.cleaned_data.get('family_password2')

            if password_form == password_form2:

                try:
                    new_family = Family.objects.create(name=family_name_form, password=password_form)
                    message="Votre famille a été correctement ajoutée, vous pouvez accéder à votre espace famille"
                
                except Family.DoesNotExist:
                    message="La saisie est incorrecte"
            
            else:
                message="Les mots de passe doivent être identiques"
            
    return render(request, 'identification.html', context={'login_form': login_form, 'registration_form': registration_form, 'message': message})
