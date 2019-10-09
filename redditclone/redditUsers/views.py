from redditclone.authentication.forms import LoginForm, SignupForm
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login


def update_bio(request):
    html = 'bio.html'
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = authenticate(username=data["username"], password=data["password"])
            if u is not None:
                login(request, u)
            else:
                return HttpResponseRedirect(reverse('login'))
            return HttpResponseRedirect(reverse('homepage'))
    form = SignupForm()

    return render(request, html, {"form": form})
