from django.shortcuts import render, HttpResponseRedirect, reverse

from redditclone.posts.forms import PostLinkForm, PostTextForm

from redditclone.posts.models import Post
from redditclone.communitys.models import Community
from redditclone.redditUsers.models import RedditUser

# def index(request, *args, **kwargs):
#     html = "Mainpage.html"

#     posts = Post.objects.all()

#     return render(request, html, {'data': posts})

def post_view(request, commun, id, *args, **kwargs):
    html = "postpage.html"

    post = Post.objects.get(id=id)

    return render(request, html, {'post': post})

def add_textpost(request, commun, *args, **kwargs):
    html = 'addtextpost.html'

    if request.method == "POST":
        form = PostTextForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                community=Community.objects.get(name=commun),
                author=RedditUser.objects.get(user=request.user),
                title=data['title'],
                text=data['text'],
            )
            return HttpResponseRedirect('/r/{}'.format(commun))
    form = PostTextForm()

    return render(request,html,{'form': form})

def add_linkpost(request, commun, *args, **kwargs):
    html = 'addlinkpost.html'

    if request.method == "POST":
        form = PostLinkForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Post.objects.create(
                community=Community.objects.get(name=commun),
                author=RedditUser.objects.get(user=request.user),
                title=data['title'],
                urls=data['urls'],
            )
            return HttpResponseRedirect('/r/{}'.format(commun))
    form = PostLinkForm()

    return render(request,html,{'form': form})

def post_community_view(request,  commun, *args, **kwargs):
    html = "communitypage.html"

    community = Community.objects.get(name=commun)
    posts = Post.objects.filter(community=community)

    return render(request, html, {'data': posts, "community": community})