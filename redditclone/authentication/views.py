from redditclone.authentication.forms import LoginForm, SignupForm
from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
# from django.db import IntegrityError
# from django.contrib.admin.views.decorators import staff_member_required

from redditclone.authentication.forms import LoginForm, SignupForm

from redditclone.redditUsers.models import RedditUser
from redditclone.posts.models import Post
from redditclone.communitys.models import Community


#@login_required()
def index(request, *args, **kwargs):

    # html = 'base.html'
    # html = "mainpage.html"
    html = 'home.html'
    community = Community.objects.all().order_by('-date')[:5]
    posts = Post.objects.filter(post_removed=False).order_by('-date')
    try:
        reddituser = RedditUser.objects.get(user=request.user)
    except:
        reddituser = ''
    return render(request, html, {'data': posts, "reddituser":reddituser, "community":community})

def all_communities(request, *args, **kwargs):

    # html = 'base.html'
    # html = "mainpage.html"
    html = 'allpage.html'
    community = Community.objects.all().order_by('-date')
    community2 = Community.objects.all().order_by('-date')[:5]
    posts = Post.objects.filter(post_removed=False)
    try:
        reddituser = RedditUser.objects.get(user=request.user)
    except:
        reddituser = ''
    return render(request, html, {'data': posts, "reddituser":reddituser, "community":community, "community2":community2})


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


class LoginView(TemplateView):
    html = 'login.html'


    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request,self.html,{'form': form})
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            u = authenticate(username=data["username"], password=data["password"])
            if u is not None:
                login(request, u)
            else:
                return HttpResponseRedirect(reverse('login'))

            destination = request.GET.get('next')
            if destination is not None:
                return HttpResponseRedirect(destination)
            else:
                return HttpResponseRedirect(reverse('homepage'))

        return render(request, self.html, {"form": form})


# def login_view(request):
#     html = 'login.html'

#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             u = authenticate(username=data["username"], password=data["password"])
#             if u is not None:
#                 login(request, u)
#             else:
#                 return HttpResponseRedirect(reverse('login'))
#             return HttpResponseRedirect(reverse('homepage'))
#     form = LoginForm()

#     return render(request, html, {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def handler404(request):
    return render(request, '404.html', status=404)

def handler500(request):
    return render(request, '500.html', status=500)