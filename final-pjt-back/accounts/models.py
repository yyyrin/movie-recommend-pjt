from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from movies.models import Review
from community.models import Article

class User(AbstractUser):
    img_path = models.TextField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTGTscNJlgpTAHrwG6kBOgIN10pNW3RX35ByBdzxwQExmQ5-Y_HQq_gMJEdDn8Jc9DIDyA&usqp=CAU')
    reported = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='reporting')

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    reviews = models.ManyToManyField(Review)
    articles = models.ManyToManyField(Article)
