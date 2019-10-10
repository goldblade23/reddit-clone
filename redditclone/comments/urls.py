from django.urls import path

from redditclone.comments.views import comments_like, comments_dislike, comments_unlike, comments_undislike, comment_delete

urlpatterns = [
   # path('r/<str:commun>/post/commentvote/like/<int:id>', comments_like),
   # path('r/<str:commun>/post/commentvote/dislike/<int:id>', comments_dislike),
   # path('r/<str:commun>/post/commentvote/unlike/<int:id>', comments_unlike),
   # path('r/<str:commun>/post/commentvote/undislike/<int:id>', comments_undislike),
   # path('r/<str:commun>/comment/delete/<int:id>',comment_delete)
]