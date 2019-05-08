from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from social import forms

__all__ = ["Register", "Profile"]


class Register(CreateView):
    form_class = forms.SocialUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


class Profile(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "user/profile.html"
