from django.urls import path
from redditclone.redditUsers.views import update_bio

urlpatterns = [
    path('bio/', update_bio)
]
