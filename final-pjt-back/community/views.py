from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Article, Comment, Community
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import CommunityListSerializer, CommuntiySerializer, ArtcleSerializer
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