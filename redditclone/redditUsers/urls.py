from django.urls import path
# from redditclone.redditUsers.views import bio
from redditclone.redditUsers.views import profile_page
urlpatterns = [
    # path('bio/', bio)
    path('profile/<str:name>/', profile_page)
]
