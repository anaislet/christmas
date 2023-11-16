from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.decorators import login_required
from authentication.models import Member, Family
from presents.models import Gift, Purchase
from django.db.models import Count
from . import forms
from datetime import datetime, timedelta


# @login_required
def home(request, member_id):

    #nom de la famille à laquelle appartient le membre qui s'est identifié
    family_name = Member.objects.get(id=member_id).family

    family_id = Member.objects.get(id=member_id).family_id

    #liste des cadeaux du membre identifié
    my_presents = Gift.objects.filter(member=member_id)

    #liste des cadeaux appartenant à un membre de la famille du membre identifié
    family_presents = Gift.objects.filter(family=family_name).select_related('member')

    #liste des membres appartenant à la famille du membre identifié y compris lui-même
    family_members = Member.objects.filter(family_id=family_name).exclude(id=member_id)

    #  Formulaire d'ajout du cadeau
    member = get_object_or_404(Member, id=member_id)
    family = get_object_or_404(Family, id=family_id)
    if request.method == 'POST':
        add_present_form = forms.AddGiftForm(request.POST)
        if add_present_form.is_valid():
            gift = add_present_form.save(commit=False)
            gift.member = member
            gift.family = family
            gift.save()
            return redirect("home", member_id)
        else:
            message = "Erreur dans le formulaire. Veuillez vérifier les données saisies."
    else:
        add_present_form = forms.AddGiftForm()
        message = ""

    #décompte
    christmas_date = datetime(2023, 12, 25)
    now = datetime.now()
    timelaps = christmas_date - now

    return render(request, 
                  'home.html',
                  {
                    'my_presents': my_presents,
                    'family_presents': family_presents,
                    'family_members': family_members,
                    'family_name': family_name,
                    'add_present_form': add_present_form,
                    'message':message,
                    'timelaps': timelaps
                  }
                )

def present_detail(request, present_id):
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

    # relevé du statut réservé ou non
    try:
        gift = Purchase.objects.get(gift=present_id)
        is_booked = True

    except Purchase.DoesNotExist:
        is_booked = False

    is_mine = str(my_present.member) == request.session['member']

    return render(request, 'present_detail.html', {'present': my_present, 'change_present_form': change_present_form, 'member_id': request.session['member_id'], 'is_mine': is_mine, 'message': message, 'is_booked': is_booked})


def delete_present(request, present_id, member_id):
    present = get_object_or_404(Gift, id=present_id)
    present.delete()
    return redirect("home", member_id)


def purchase_present(request, present_id, member_id):
    member = get_object_or_404(Member, id=member_id)
    gift = get_object_or_404(Gift, id=present_id)

    new_purchase = Purchase.objects.create(member=member, gift=gift)
    return redirect("shopping-list", member_id)


def shopping_list(request, member_id):
    my_booked_gifts = Purchase.objects.filter(member=member_id)
    all_gift_infos = [my_booked_gift.gift for my_booked_gift in my_booked_gifts]
    return render(request, 'shopping_list.html', {'all_gift_infos': all_gift_infos})


def delete_purchase(request, present_id, member_id):
    purchase = get_object_or_404(Purchase, gift=present_id)
    purchase.delete()
    return redirect("shopping-list", member_id)