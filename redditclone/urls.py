"""redditclone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin

from redditclone.authentication.views import index
from redditclone.redditUsers.models import RedditUser
from redditclone.communitys.models import Community
from redditclone.posts.models import Post
from redditclone.comments.models import Comment
from redditclone.notifications.models import Notification

# from redditclone.authentication.urls import urlpatterns as auth_urls
# from redditclone.redditUsers.urls import urlpatterns as redditusers_urls
from redditclone.communitys.urls import urlpatterns as communitys_urls
from redditclone.posts.urls import urlpatterns as posts_urls
# from redditclone.comments.urls import urlpatterns as comments_urls
# from redditclone.notifications.urls import urlpatterns as notification_urls

admin.site.register(RedditUser)
admin.site.register(Community)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Notification)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="homepage"),
    
]

# urlpatterns += auth_urls
# urlpatterns += redditusers_urls
urlpatterns += communitys_urls
urlpatterns += posts_urls
# urlpatterns += comments_urls
# urlpatterns += notification_urls