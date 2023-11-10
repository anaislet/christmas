from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentication.models import Member
from presents.models import Gift
from django.db.models import Count


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