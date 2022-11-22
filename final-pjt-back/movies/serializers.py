from rest_framework import serializers
from .models import Movie, Review, Genre, Director, Actor, Preference_movies
from django.contrib.auth import get_user_model

class MovieListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'


class ReviewSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')

    user = UserSerializer(read_only=True)
    movie = MovieListSerializer(read_only=True)
    like_user = UserSerializer(many=True, read_only=True)

    class Meta:
        model = Review
        fields = '__all__'


class MovieDetailSerializer(serializers.ModelSerializer):
    review_set = ReviewSerializer(many=True, read_only=True)
    
    class Meta:
        model = Movie
        fields = '__all__'

class ActorProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        fields = '__all__'

class DirectorProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Director
        fields = '__all__'


class GerneSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'