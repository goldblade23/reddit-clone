from django import forms
from django.forms import ModelForm

from redditclone.posts.models import Post

class PostTextForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']

class PostLinkForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'urls']