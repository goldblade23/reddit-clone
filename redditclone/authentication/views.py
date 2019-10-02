from redditclone.authentication.forms import LoginForm, SignupForm
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.db import IntegrityError
# from django.contrib.admin.views.decorators import staff_member_required


def index(request, *args, **kwargs):
    html = 'base.html'
    return render(request, html)


def signup(request):
    html = 'signup.html'
    form = None
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(
                data["username"], data["password"])
            login(request, user)
            user.objects.create(
                name=data["name"],
                bio=data["bio"],
                birthday=["birthday"],
                displayname=["display name"],
                user=user
            )
            return HttpResponseRedirect(reverse("homepage"))
    else:
        form = SignupForm()
    return render(request, html, {"form": form})


def login_view(request):
    html = 'login.html'
    form = None
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(request.GET.get("next", "/"))
    else:
        form = LoginForm()
    return render(request, html, {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('homepage'))
