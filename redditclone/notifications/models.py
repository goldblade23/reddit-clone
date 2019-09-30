from django.db import models
from django.contrib.auth.models import User

from redditclone.redditUsers.models import RedditUser
from redditclone.comments.models import Comment


class Notification(models.Model):
    reddit_user = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    comment =  models.ForeignKey(Comment, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    
    def __str__(self):
        return f"to: {self.reddit_user} - {self.post.text} - from: {self.reddituser_user.displayname}"