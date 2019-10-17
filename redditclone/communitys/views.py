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
            )
            community = Community.objects.get(id=Community.objects.all().count())
            community.moderators.add(logged_in_user)
            community.subscriber.add(logged_in_user)
        return HttpResponseRedirect('/r/{}'.format(community.name))
    form = CommunityForm()

    return render(request, html, {'form': form})

def subscribe(request, commun, *args, **kwargs):
    reddit_user = RedditUser.objects.get(user=request.user)
    
    try:
        community = Community.objects.get(name=commun)
        
    except Community.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # return HttpResponseRedirect(reverse('homepage'))

    community.subscriber.add(reddit_user)
 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def unsubscribe(request, commun, *args, **kwargs):
    reddit_user = RedditUser.objects.get(user=request.user)
    
    try:
        community = Community.objects.get(name=commun)
        
    except Community.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        # return HttpResponseRedirect(reverse('homepage'))

    community.subscriber.remove(reddit_user)
 
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))