from django.urls import path
from redditclone.redditUsers.views import bio

urlpatterns = [
    path('bio/', bio)
]
