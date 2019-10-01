from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required

from redditclone.communitys.forms import CommunityForm

from redditclone.redditUsers.models import RedditUser
from redditclone.communitys.models import Community

@login_required()
def add_community(request, *args, **kwargs):
    html = 'addcommunity.html'
    logged_in_user = RedditUser.objects.get(user=request.user)
    
    if request.method == "POST":
        form = CommunityForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Community.objects.create(
                creator=logged_in_user,
                name=data['name'],
                description=data['description'],
                rules=data['rules']
            )
            community = Community.objects.get(id=Community.objects.all().count())
            community.moderators.add(logged_in_user)
            community.subscriber.add(logged_in_user)
        return HttpResponseRedirect('/r/{}'.format(community.name))
    form = CommunityForm()

    return render(request,html,{'form': form})


    