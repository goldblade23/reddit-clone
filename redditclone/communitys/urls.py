from django.urls import path

from redditclone.communitys.views import add_community

urlpatterns = [
   path('createcommunity/', add_community)
]