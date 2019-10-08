# dev test
from django.db import models
from django.contrib.auth.models import User

from redditclone.communitys.models import Community
from redditclone.redditUsers.models import RedditUser
# from redditclone.comments.models import Comment



class Post(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    urls = models.URLField(max_length=250)
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=200)
    author = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True,blank=True)
    post_likes = models.ManyToManyField(RedditUser, related_name="post_likes")
    post_dislikes = models.ManyToManyField(RedditUser, related_name="post_dislikes")
    
    def __str__(self):
        return f"{self.title} - {self.author.displayname}"

    def get_comment_count(self):
        from redditclone.comments.models import Comment
        return Comment.objects.filter(post=self).count()

    def post_likes_count(self):
        return self.post_likes.all().count() - self.post_dislikes.all().count()
