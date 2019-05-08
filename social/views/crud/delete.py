from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView

from social import models

__all__ = ["DeletePost", "DeleteLink", "DeleteSnippet"]


class SharableDelete(DeleteView):
    def __init_subclass__(cls):
        simple_name = cls.__name__.replace("Delete", "").lower()

        cls.model = getattr(models, f"{simple_name.title()}")
        cls.success_url = reverse_lazy("home")
        cls.template_name = f"forms/delete/{simple_name}.html"

        super().__init_subclass__()

    def delete(self, request, *args, **kwargs):
        if self.get_object().author == request.user:
            return super().delete(request, *args, **kwargs)
        else:
            return HttpResponse("Unauthorized", status=401)


class DeletePost(SharableDelete):
    pass


class DeleteLink(SharableDelete):
    pass


class DeleteSnippet(SharableDelete):
    pass
