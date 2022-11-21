from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from movies.models import Review
from community.models import Article

class User(AbstractUser):
    img_path = models.CharField(max_length=100, null=True)

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reviews = models.ManyToManyField(Review)
    articles = models.ManyToManyField(Article)