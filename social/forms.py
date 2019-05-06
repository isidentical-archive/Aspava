from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django_ace import AceWidget

from social.models import Post, Link, Snippet


class SocialUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "avatar")

class SocialUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "email", "avatar")

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("text",)

class CreateSnippetForm(forms.ModelForm):
    class Meta:
        model = Snippet
        fields = ("text",)
        widgets = {
            "text": AceWidget(mode='python', theme='monokai'),
        }
        
class CreateLinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ("url",)
