from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer
from .models import Movie



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_list(request):
    if request.method == 'GET':
        Movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(Movies, many=True)
        return Response(serializer.data)
