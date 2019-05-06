from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model

from social.models import Post, Link, Snippet


class SocialUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "avatar")

class SocialUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "avatar")

class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("text",)

class SnippetCreationForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ("text",)
        
class LinkCreationForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ("url",)
