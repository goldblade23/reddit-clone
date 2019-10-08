from django.urls import path

from redditclone.posts.views import post_community_view, add_linkpost, add_textpost, post_view, post_like, post_dislike, post_unlike, post_undislike

urlpatterns = [
   # path('', index),
   path('r/<str:commun>', post_community_view),
   path('r/<str:commun>/addlinkpost', add_linkpost),
   path('r/<str:commun>/addtextpost', add_textpost),
   path('r/<str:commun>/post/<int:id>', post_view),
   path('r/<str:commun>/post/postvote/like/<int:id>', post_like),
   path('r/<str:commun>/post/postvote/dislike/<int:id>', post_dislike),
   path('r/<str:commun>/post/postvote/unlike/<int:id>', post_unlike),
   path('r/<str:commun>/post/postvote/undislike/<int:id>', post_undislike),
]
