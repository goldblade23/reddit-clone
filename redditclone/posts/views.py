from django.shortcuts import render, HttpResponseRedirect, reverse

from redditclone.posts.forms import PostForm

from redditclone.posts.models import Post
from redditclone.communitys.models import Community

def index(request, *args, **kwargs):
    html = "Mainpage.html"

    posts = Post.objects.all()

    return render(request, html, {'data': posts})


def post_community_view(request,  commun, *args, **kwargs):
    html = "communitypage.html"

    community = Community.objects.get(name=commun)
    posts = Post.objects.filter(community=community)

    return render(request, html, {'data': posts, "community": community})