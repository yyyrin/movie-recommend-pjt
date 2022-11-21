from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import ImgSerializer, ProfileSerializer
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
