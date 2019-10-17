from django.urls import path

from redditclone.communitys.views import add_community, subscribe, unsubscribe

urlpatterns = [
   path('createcommunity/', add_community),
   path('r/<str:commun>/subsribe', subscribe),
   path('r/<str:commun>/unsubsribe', unsubscribe)
]