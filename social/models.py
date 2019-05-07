from pathlib import Path
from random import randint
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db import models

def get_avatar():
    return settings.STATIC_URL / Path(settings.AVATAR_BASE.format(randint(1, 4)))
    
class SocialUser(AbstractUser):
    avatar = models.URLField(blank=True, default=get_avatar)
    desc = models.TextField(blank=True, default=settings.DESC)

    @property
    def slug(self):
        return self.username


class Sharable(models.Model):
    class Meta:
        ordering = ["pub_date"]

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    pub_date = models.TimeField(auto_now=True)

    def __str__(self):
        return f"{self.__class__.__name__}@{self.author}"


class Post(Sharable):
    text = models.TextField(max_length=settings.MAX_POST_LENGTH)


class Snippet(Sharable):
    text = models.TextField()


class Link(Sharable):
    url = models.URLField()
