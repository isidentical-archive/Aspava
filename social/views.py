from itertools import chain

from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.base import TemplateView

from social.models import Link, Post, Snippet
from social.forms import SocialUserCreationForm

class ExtendedListView(ListView):
    def get_queryset(self):
        return chain.from_iterable(
            map(lambda model: model._default_manager.all(), self.models)
        )


class Home(ExtendedListView):
    models = Post, Snippet, Link
    template_name = "home.html"
    context_object_name = "feed"

    def get_queryset(self):
        qs = list(super().get_queryset())
        qs.sort(key=(lambda item: item.pub_date))
        return qs


class Register(CreateView):
    form_class = SocialUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"


class Profile(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "user/profile.html"
