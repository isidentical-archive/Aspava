import docker
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

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

    def get_queryset(self):
        qs = list(super().get_queryset())
        qs.sort(key=(lambda item: item.id))
        return reversed(qs)

@csrf_exempt
def run_snippet(request):
    snippet = get_object_or_404(Snippet, pk = request.POST.get('pk', None))
    global evality
    try:
        result = evality.run_cmd(snippet.text, snippet.author.id)
    except docker.exceptions.DockerException:
        evality.quit()

    result['id'] = snippet.id
    return JsonResponse(result)
