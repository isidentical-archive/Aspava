from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class SocialUser(AbstractUser):
    pass
    
class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
