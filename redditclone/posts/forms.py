from django import forms
from django.forms import ModelForm

from redditclone.posts.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']