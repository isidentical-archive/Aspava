from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.base import TemplateView
from purima.views import ExtendedListView

from social.models import Link, Post, Snippet
from social.forms import PostCreationForm, SocialUserCreationForm

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

class Post(CreateView):
    form_class = PostCreationForm
    success_url = reverse_lazy("home")
    template_name = "forms/post.html"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
class Profile(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "user/profile.html"
