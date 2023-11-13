from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from authentication.models import Member
from presents.models import Gift
from django.db.models import Count
from . import forms


# @login_required
def home(request, member_id):

    #nom de la famille à laquelle appartient le membre qui s'est identifié
    family_id = Member.objects.get(id=member_id).family

    #liste des cadeaux du membre identifié
    my_presents = Gift.objects.filter(member=member_id)

    #liste des cadeaux appartenant à un membre de la famille du membre identifié
    family_presents = Gift.objects.filter(family=family_id).select_related('member')

    #liste des membres appartenant à la famille du membre identifié y compris lui-même
    family_members = Member.objects.filter(family_id=family_id).exclude(id=member_id)

    return render(request, 
                  'home.html',
                  {'my_presents': my_presents, 'family_presents': family_presents, 'family_members': family_members}
                )

def my_list(request):
    return render(request, 'mylist.html')

def present_detail(request, present_id):
    print(request.session['member_id'])
    my_present = Gift.objects.get(id=present_id)

    #Formulaire de modification du cadeau
    present = get_object_or_404(Gift, id=present_id)

    if request.method == 'POST':
        change_present_form = forms.ModifyGiftForm(request.POST, instance=present)
        if change_present_form.is_valid():
            change_present_form.save()
            return redirect("present-detail", present_id)
        else:
            message = "Erreur dans le formulaire. Veuillez vérifier les données saisies."
    else:
        change_present_form = forms.ModifyGiftForm(instance=present)
        message = ""
    
    #Suppression du cadeau
    ############################################################################################
    return render(request, 'present_detail.html', {'present': my_present, 'change_present_form': change_present_form, 'member_id': request.session['member_id'], 'message': message})
