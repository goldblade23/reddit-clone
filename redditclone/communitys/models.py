from django.db import models
from django.contrib.auth.models import User

from redditclone.redditUsers.models import RedditUser

class Community(models.Model):
    creator = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    moderators = models.ManyToManyField(RedditUser, related_name="moderator")
    description = models.TextField(max_length=200)
    rules = models.TextField(max_length=200)
    banlist = models.ManyToManyField(RedditUser, related_name="banned")
    subscriber = models.ManyToManyField(RedditUser, related_name="subsribers")

    def __str__(self):
        return f"{self.name} - {self.creator.displayname}"