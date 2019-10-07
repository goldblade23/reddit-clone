from django.urls import path

from redditclone.posts.views import post_community_view, add_linkpost, add_textpost, post_view

urlpatterns = [
   # path('', index),
   path('r/<str:commun>', post_community_view),
   path('r/<str:commun>/addlinkpost', add_linkpost),
   path('r/<str:commun>/addtextpost', add_textpost),
   path('r/<str:commun>/post/<int:id>', post_view),
]
