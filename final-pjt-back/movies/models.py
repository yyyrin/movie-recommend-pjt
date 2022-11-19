from django.db import models
from django.conf import settings



class Genre(models.Model):
    name = models.CharField(max_length=50)

class Actor(models.Model):
    name= models.CharField(max_length=50)
    profile_path= models.CharField(max_length=100, null=True)

class Director(models.Model):
    name= models.CharField(max_length=50)
    profile_path= models.CharField(max_length=100, null=True)

class Movie(models.Model):
    title = models.CharField(max_length=100)
    overview = models.TextField()
    poster_path = models.CharField(max_length=100)
    release_date = models.DateField()
    vote_average = models.FloatField()
    vote_count = models.IntegerField()
    runtime = models.IntegerField()
    genres = models.ManyToManyField(Genre)
    trailer = models.CharField(max_length=100)
    actors = models.ManyToManyField(Actor)
    director = models.ManyToManyField(Director)


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    rate = models.IntegerField()
    like_user = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_review')

class Preference_movies(models.Model):
    user_id = models.IntegerField()
    movie1 = models.IntegerField()
    movie2 = models.IntegerField()
    movie3 = models.IntegerField()
    movie4 = models.IntegerField()