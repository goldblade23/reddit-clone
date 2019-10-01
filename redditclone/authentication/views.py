from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout


def index(request, *args, **kwargs):
    html = 'base.html'
    return render(request, html)
