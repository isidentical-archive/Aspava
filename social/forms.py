from django import forms
from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django.contrib.auth import get_user_model
from django_ace import AceWidget
from captcha.fields import CaptchaField

from social.models import Post, Link, Snippet

    
class SocialUserCreationForm(UserCreationForm):
    captcha = CaptchaField()
    class Meta:
        model = get_user_model()
        fields = ("username", "email")

class SocialUserChangeForm(UserChangeForm):
    captcha = CaptchaField()
    class Meta:
        model = get_user_model()
        fields = ("username", "email")

class CreateSharedForm(forms.ModelForm):
    captcha = CaptchaField()
    
class CreatePostForm(CreateSharedForm):
    captcha = CaptchaField()
    class Meta:
        model = Post
        fields = ("text",)

class CreateSnippetForm(CreateSharedForm):
    captcha = CaptchaField()
    class Meta:
        model = Snippet
        fields = ("text",)
        widgets = {
            "text": AceWidget(mode='python', theme='monokai'),
        }
        
class CreateLinkForm(CreateSharedForm):
    captcha = CaptchaField()
    class Meta:
        model = Link
        fields = ("url",)
