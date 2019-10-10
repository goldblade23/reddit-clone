# from django.db import models

# from redditclone.redditUsers.models import RedditUser
# from redditclone.communitys.models import Community

# class Message(models.Model):
#     message_to = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
#     message_from = models.ForeignKey(RedditUser, on_delete=models.CASCADE)
#     text = models.TextField(max_length=200)
#     mod_invite = models.BooleanField(default=False)
#     community = models.ManyToManyField(Community, on_delete=models.CASCADE)
#     seen = models.BooleanField(default=False)
#     answered = models.BooleanField(default=False)

#     def __str__(self):
#         return f"{self.message_to} - {self.message_from}"
    