from django.urls import path
# from redditclone.redditUsers.views import bio
from redditclone.redditUsers.views import profile_page, profile_page_comments
urlpatterns = [
    # path('bio/', bio)
    path('profile/<str:name>/', profile_page),
    path('profile/<str:name>/comments', profile_page_comments)
]
