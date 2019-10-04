from django import forms
from django.forms import ModelForm

from redditclone.comments.models import Comment

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class ReplyForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']