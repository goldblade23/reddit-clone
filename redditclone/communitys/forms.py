from django import forms
from django.forms import ModelForm

from redditclone.communitys.models import Community

class CommunityForm(ModelForm):
    class Meta:
        model = Community
        fields = ['name', 'description', 'rules']