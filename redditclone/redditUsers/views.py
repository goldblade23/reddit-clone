from redditclone.authentication.forms import LoginForm, SignupForm
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from redditclone.redditUsers.forms import UpdateUser
from django.contrib.auth.decorators import login_required


@login_required()
def bio(request):
    html = 'bio.html'
    #logged_in_user = RedditUser.objects.get(user=request.user)

    return render(request, html)
