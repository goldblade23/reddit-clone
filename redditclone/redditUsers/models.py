from django.db import models
from django.contrib.auth.models import User

class RedditUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    displayname = models.CharField(max_length=30)
    bio = models.TextField(max_length=200)
    birthday = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.displayname