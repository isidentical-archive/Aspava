import docker
import docker.errors
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils import timezone
from datetime import datetime, timedelta
from functools import partial

from evality import Evality
from purima.views import ExtendedListView
from social.models import Link, Post, Snippet
from social.views.auth import *
from social.views.crud import *

docker_client = docker.from_env()
api_client = docker.APIClient(base_url="unix://var/run/docker.sock")
evality = Evality(docker_client, api_client)

class Home(ExtendedListView):
    models = Post, Snippet, Link
    template_name = "home.html"
    context_object_name = "feed"

    def date_sorted(self, qs, to_date, from_date):
        return list(filter(lambda item: from_date < item.pub_date < to_date, qs))

    def get_queryset(self):
        qs = list(super().get_queryset())
        qs.sort(key=(lambda item: item.vote_total))
        return reversed(qs)
    
    def get_context_data(self):
        context = super().get_context_data()
        context['all_time'] = list(context.pop(self.context_object_name))
        
        now = timezone.now()
        date_sorted = partial(self.date_sorted, context['all_time'], now)
        
        context['this_year'] = date_sorted(now - timedelta(365))
        context['this_month'] = date_sorted(now - timedelta(30))
        context['this_week'] = date_sorted(now - timedelta(7))
        context['this_day'] = date_sorted(now - timedelta(1))

        return context

@csrf_exempt
def run_snippet(request):
    snippet = get_object_or_404(Snippet, pk = request.POST.get('pk', None))
    global evality
    try:
        result = evality.run_cmd(snippet.text, snippet.author.id)
    except docker.errors.DockerException:
        evality.quit()

    result['id'] = snippet.id
    return JsonResponse(result)
