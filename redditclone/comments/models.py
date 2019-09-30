from django.db import models
from django.contrib.auth.models import User

from redditclone.posts.models import Post
from redditclone.redditUsers.models import RedditUser


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    reply = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    comment_likes = models.ManyToManyField(RedditUser, related_name="comment_likes")
    comment_dislikes = models.ManyToManyField(RedditUser, related_name="comment_dislikes")

    def __str__(self):
        return f"{self.text} - {self.commenter.displayname}"
