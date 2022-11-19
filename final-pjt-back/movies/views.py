from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, ReviewSerializer, MovieDetailSerializer, ActorProfileSerializer, DirectorProfileSerializer
from .models import Movie, Review, Genre, Actor, Director
from django.conf import settings


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def review_list(request):
    if request.method == 'GET':
        reviews = get_list_or_404(Review)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def search(request, query):
    if request.method == 'GET':
        all_movies = get_list_or_404(Movie)
        gernes = get_list_or_404(Genre)
        actors = get_list_or_404(Actor)
        directors = get_list_or_404(Director)
        movies = []
        for movie in all_movies:
            if query in movie.title or query in movie.overview:
                movies.append(movie)

        for gerne in gernes:
            if gerne.name == query:
                temp = gerne.movie_set.all()
                for movie in temp:
                    movies.append(movie)
                temp = []

        for actor in actors:
            if query in actor.name:
                temp = actor.movie_set.all()
                for movie in temp:
                    movies.append(movie)
                temp = []

        for director in directors:
            if query in director.name:
                temp = director.movie_set.all()
                for movie in temp:
                    movies.append(movie)
                temp = []

        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def profile(request, query):
    if Actor.objects.filter(name=query):
        serializer = ActorProfileSerializer(Actor.objects.filter(name=query)[0])
        return Response(serializer.data)
    elif Director.objects.filter(name=query):
        serializer = DirectorProfileSerializer(Director.objects.filter(name=query)[0])
        return Response(serializer.data)
