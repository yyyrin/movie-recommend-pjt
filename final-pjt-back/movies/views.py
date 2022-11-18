from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, ReviewSerializer, MovieDetailSerializer
from .models import Movie, Review
from django.conf import settings


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        Movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(Movies, many=True)
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
    print(movie_pk)
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
        serializer.save(movie=movie)
        serializer.save(user=request.user)
        print(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)