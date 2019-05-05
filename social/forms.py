from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm

from social.models import SocialUser


class SocialUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = SocialUser
        fields = ("username", "email")


class SocialUserChangeForm(UserChangeForm):
    class Meta:
        model = SocialUser
        fields = ("username", "email")
