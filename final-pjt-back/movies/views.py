from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, ReviewSerializer, MovieDetailSerializer, ActorProfileSerializer, DirectorProfileSerializer
from .models import Movie, Review, Genre, Actor, Director, Preference_movies
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


@api_view(['GET', 'DELETE', 'PUT'])
#@permission_classes([IsAuthenticated])
def review_detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    elif request.method == 'DELETE' and review.user == request.user:
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT' and review.user == request.user:
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def review_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, movie=movie)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def review_like(request, movie_pk, review_pk):
    response_body = {'result': ""}
    review = get_object_or_404(Review, pk=review_pk)
    if review.like_user.filter(pk=request.user.pk).exists():
        review.like_user.remove(request.user)
        response_body['result'] = 0
    else:
        review.like_user.add(request.user)
        response_body['result'] = 1
    return Response(response_body, status=status.HTTP_200_OK)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def search(request, query):
    if request.method == 'GET':
        all_movies = get_list_or_404(Movie)
        gernes = get_list_or_404(Genre)
        actors = get_list_or_404(Actor)
        directors = get_list_or_404(Director)
        movies = []
        for gerne in gernes:
            if gerne.name == query:
                temp = gerne.movie_set.all()
                for movie in temp:
                    movies.append(movie)
                temp = []
                break
        else:
            for movie in all_movies:
                if query in movie.title or query in movie.overview:
                    movies.append(movie)

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


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def preference(request, query):
    arr = list(map(int, query.split()))
    Preference_movies.objects.create(user_id=request.user.pk, movie1=arr[0],movie2=arr[1],movie3=arr[2],movie4=arr[3],)

    return Response({'reseult':1}, status=status.HTTP_201_CREATED)