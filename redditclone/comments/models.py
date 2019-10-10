from django.db import models
from django.contrib.auth.models import User

from mptt.models import MPTTModel, TreeForeignKey

from redditclone.posts.models import Post
from redditclone.redditUsers.models import RedditUser


class Comment(MPTTModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    commenter = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    text = models.TextField(max_length=200)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True,blank=True)
    comment_removed = models.BooleanField(default=False)
    comment_likes = models.ManyToManyField(RedditUser, related_name="comment_likes")
    comment_dislikes = models.ManyToManyField(RedditUser, related_name="comment_dislikes")

    def __str__(self):
        return f"{self.text} - {self.commenter.displayname}"

    def comment_likes_count(self):
        return self.comment_likes.all().count() - self.comment_dislikes.all().count()

    class MPTTMeta:
        order_insertion_by = ['-date']
