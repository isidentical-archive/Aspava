from django.urls import reverse_lazy
from django.views.generic import CreateView
from social import forms

__all__ = ['CreatePost', 'CreateLink', 'CreateSnippet']

class SharableCreate(CreateView):
    def __init_subclass__(cls):
        cls.form_class = getattr(forms, f"{cls.__name__}Form")
        cls.success_url = reverse_lazy("home")
        cls.template_name = f"forms/create/{cls.__name__.replace('Create', '').lower()}.html"
        super().__init_subclass__()
        
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class CreatePost(SharableCreate):
    pass

class CreateLink(SharableCreate):
    pass

class CreateSnippet(SharableCreate):
    pass
