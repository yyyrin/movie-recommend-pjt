from django.db import models
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