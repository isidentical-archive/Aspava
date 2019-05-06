from social.views.crud import *
from social.views.auth import *

from purima.views import ExtendedListView
from social.models import Link, Post, Snippet

class Home(ExtendedListView):
    models = Post, Snippet, Link
    template_name = "home.html"
    context_object_name = "feed"

    def get_queryset(self):
        qs = list(super().get_queryset())
        qs.sort(key=(lambda item: item.id))
        return reversed(qs)
