from django.db import models
from django.contrib.auth.models import User


class RedditUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    displayname = models.CharField(max_length=30)
    birthdate = models.DateField(auto_now=False, auto_now_add=False)
    bio = models.TextField(max_length=200)

    def __str__(self):
        return self.displayname

    #  def date_only(self):
    #     return self.birthdate.date()

