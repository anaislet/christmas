from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from authentication.models import Member
from presents.models import Gift

# @login_required
def home(request, member_id):

    family_id = Member.objects.get(id=member_id).family
    my_presents = Gift.objects.filter(member=member_id)
    family_presents = Gift.objects.filter(family=family_id)
    family_members = Member.objects.filter(family_id=family_id)
    return render(request, 
                  'home.html',
                  {'my_presents': my_presents, 'family_presents': family_presents, 'family_members': family_members}
                )

def my_list(request):
    return render(request, 'mylist.html')