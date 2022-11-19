from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article, Comment, Community
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import CommunityListSerializer, CommuntiySerializer, ArticleSerializer, CommentSerializer
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated



@api_view(['GET', 'POST'])
#@permission_classes([IsAuthenticated])
def community_list(request):
    if request.method == 'GET':
        communities = get_list_or_404(Community)
        serializer = CommunityListSerializer(communities, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = CommuntiySerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'DELETE', 'PUT'])
#@permission_classes([IsAuthenticated])
def community_detail(request, community_pk):
    print(request)
    community = get_object_or_404(Community, pk=community_pk)

    if request.method == 'GET':
        serializer = CommuntiySerializer(community)
        return Response(serializer.data)
    
    elif request.method == 'DELETE' and request.user == community.user:
        community.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT' and request.user == community.user:
        serializer = CommuntiySerializer(community, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['GET', 'DELETE', 'PUT'])
#@permission_classes([IsAuthenticated])
def article_detail(request, community_pk, article_pk):
    communtiy = get_object_or_404(Community, pk=community_pk)
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    elif request.method == 'DELETE' and (article.user == request.user or communtiy.user == article.user):
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT' and (article.user == request.user or communtiy.user == article.user):
        serializer = ArticleSerializer(article, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def article_create(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, community=community)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def comment_create(request, community_pk, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
#@permission_classes([IsAuthenticated])
def article_like(request, community_pk, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    response_body = {'result': ""}
    if article.like_users.filter(pk=request.user.pk).exists():
        article.like_users.remove(request.user)
        response_body['result'] = 0
    else:
        article.like_users.add(request.user)
        response_body['result'] = 1
    return Response(response_body, status=status.HTTP_200_OK)


@api_view(['GET', 'DELETE', 'PUT'])
#@permission_classes([IsAuthenticated])
def comment_detail(request, community_pk, article_pk, comment_pk):
    communtiy = get_object_or_404(Community, pk=community_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'GET':
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    elif request.method == 'DELETE' and (comment.user == request.user or communtiy.user == comment.user):
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    elif request.method == 'PUT' and (comment.user == request.user or communtiy.user == comment.user):
        serializer = CommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)