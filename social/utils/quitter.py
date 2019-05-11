import docker.errors
from contextlib import suppress

def quit_evality():
    from social.views import evality, docker_client
    evality.quit()
    for container in docker_client.containers.list():
        if "evality:latest" in container.image.tags:
            with suppress(docker.errors.DockerException):
                container.kill()
