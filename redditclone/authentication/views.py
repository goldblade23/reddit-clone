from redditclone.authentication.forms import LoginForm, SignupForm
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# from django.db import IntegrityError
# from django.contrib.admin.views.decorators import staff_member_required

from redditclone.authentication.forms import LoginForm, SignupForm

from redditclone.redditUsers.models import RedditUser
from redditclone.posts.models import Post


#@login_required()
def index(request, *args, **kwargs):

    # html = 'base.html'
    # html = "mainpage.html"
    html = 'home.html'

    posts = Post.objects.all()
    try:
        reddituser = RedditUser.objects.get(user=request.user)
    except:
        reddituser = ''
    return render(request, html, {'data': posts, "reddituser":reddituser})


def signup(request):
    html = 'signup.html'

    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = User.objects.create_user(username=data['username'], password=data['password'])
            RedditUser.objects.create(
                user=u,
                displayname=data["displayname"],
                bio=data["bio"],
                birthdate=data["birthdate"]
            )
            login(request, u)
            return HttpResponseRedirect(reverse("homepage"))
    form = SignupForm()
    
    return render(request, html, {"form": form})


def login_view(request):
    html = 'login.html'

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = authenticate(username=data["username"], password=data["password"])
            if u is not None:
                login(request, u)
            else:
                return HttpResponseRedirect(reverse('login'))
            return HttpResponseRedirect(reverse('homepage'))
    form = LoginForm()

    return render(request, html, {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))

