from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class SocialUser(AbstractUser):
    pass
    
class Post(models.Model):
    
    class Meta:
        ordering = ['pub_date']
        
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    
    text = models.TextField(max_length=settings.MAX_POST_LENGTH)
    pub_date = models.TimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}#{self.id}"
