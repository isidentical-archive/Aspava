from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView
from django.views.generic.base import TemplateView
from social.models import Post, Snippet

from operator import or_
from functools import wraps, reduce

def ret_or_super(func):
    def wrapper(*args, **kwargs):
        try:
            res = func(*args, **kwargs)
        except:
            self = args[0]
            res = getattr(super(self.__class__, self), func.__name__)(*args, **kwargs)
        
        return res
        
    return wrapper

class ExtendedListView(ListView):
    def get_queryset(self):
        queryset = reduce(or_, map(lambda model: model._default_manager.all(), self.models))
        return queryset
        
    
class Home(ExtendedListView):
    models = Post, Snippet
    template_name = 'home.html'
    context_object_name = 'feed'
    
class Register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'
