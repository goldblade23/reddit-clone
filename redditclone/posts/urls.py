from django.urls import path

# from redditclone.posts.views import post_community_view, index

urlpatterns = [
   # path('', index),
   path('r/<str:commun>', post_community_view)
]