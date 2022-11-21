from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ImgSerializer, ProfileSerializer, ReportSerializer, StopSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated
from community.serializers import ArticleSerializer
from movies.serializers import ReviewSerializer
from movies.models import Review
from community.models import Article
from django.contrib.auth import get_user_model


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def profile(request, user_pk):
    if request.method == 'GET':
        reviews = get_list_or_404(Review, user=request.user)
        articles = get_list_or_404(Article, user=request.user)
        print(reviews)
        print(articles)
        user = get_object_or_404(get_user_model(), pk=user_pk)
        print(user.pk)
        print(request.data)
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=user, reviews=reviews,articles=articles)
            return Response(serializer.data, status=status.HTTP_200_OK)

    

@api_view(['GET', 'DELETE', 'PUT'])
#@permission_classes([IsAuthenticated])
def img_change(request, user_pk):
    user = get_object_or_404(get_user_model(), pk=request.user.pk)
    if request.method == 'GET':
        serializer = ImgSerializer(user)
        return Response(serializer.data)
    elif request.method == 'DELETE' and request.user == user:
        serializer = ImgSerializer(user, data={'img_path':''})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT' and request.user == user:
        serializer = ImgSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def report(request, user_pk):
    if request.method == 'POST':
        user = get_object_or_404(get_user_model(), pk=user_pk)
        if not user.reported.filter(pk=request.user.pk).exists():
            if user.reported.count() >= 2:
                serializer = StopSerializer(user, data={'is_active':0})
                if serializer.is_valid(raise_exception=True):
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'is_active': 1}, status=status.HTTP_201_CREATED)