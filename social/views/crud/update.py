from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from social import forms, models

__all__ = ["UpdatePost", "UpdateLink", "UpdateSnippet"]


class SharableUpdate(UpdateView):
    def __init_subclass__(cls):
        simple_name = cls.__name__.replace("Update", "").lower()

        cls.model = getattr(models, f"{simple_name.title()}")
        cls.success_url = reverse_lazy("home")
        cls.template_name = f"forms/update/{simple_name}.html"
        cls.form_class = getattr(forms, f"Create{simple_name.title()}Form")
        super().__init_subclass__()

    def form_valid(self, *args, **kwargs):
        if self.get_object().author == self.request.user:
            return super().form_valid(*args, **kwargs)
        else:
            return HttpResponse("Unauthorized", status=401)


class UpdatePost(SharableUpdate):
    pass


class UpdateLink(SharableUpdate):
    pass


class UpdateSnippet(SharableUpdate):
    pass
