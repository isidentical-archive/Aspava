from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView
from django.views.generic.base import TemplateView
from purima.views import ExtendedListView

from social import forms
from social.models import Link, Post, Snippet
class Home(ExtendedListView):
    models = Post, Snippet, Link
    template_name = "home.html"
    context_object_name = "feed"

    def get_queryset(self):
        qs = list(super().get_queryset())
        qs.sort(key=(lambda item: item.pub_date))
        return qs


class Register(CreateView):
    form_class = forms.SocialUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"

class SharableCreate(CreateView):
    def __init_subclass__(cls):
        cls.form_class = getattr(forms, f"{cls.__name__}CreationForm")
        cls.success_url = reverse_lazy("home")
        cls.template_name = f"forms/{cls.__name__.lower()}.html"
        super().__init_subclass__()
        
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
        
class Post(SharableCreate):
    pass

class Link(SharableCreate):
    pass

class Snippet(SharableCreate):
    pass

    
class Profile(DetailView):
    model = get_user_model()
    slug_field = "username"
    template_name = "user/profile.html"
