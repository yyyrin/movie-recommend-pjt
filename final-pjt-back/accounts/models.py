from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from movies.models import Review
from community.models import Article

class User(AbstractUser):
    img_path = models.TextField(default='https://emojigraph.org/media/microsoft/honeybee_1f41d.png')
    reported = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='reporting')

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reviews = models.ManyToManyField(Review)
    articles = models.ManyToManyField(Article)
