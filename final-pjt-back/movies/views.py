from rest_framework.response import Response
from rest_framework.decorators import api_view

from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

from rest_framework import status
from django.shortcuts import get_object_or_404, get_list_or_404
from .serializers import MovieListSerializer, ReviewSerializer, MovieDetailSerializer, ActorProfileSerializer, DirectorProfileSerializer, GerneSerializer
from .models import Movie, Review, Genre, Actor, Director, Preference_movies
from django.contrib.auth import get_user_model


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


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def recommand(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        reviews = get_list_or_404(Review)
        users = get_list_or_404(get_user_model())
        #preferences = get_list_or_404(Preference_movies)
        movie_id_arr =[]
        user_id_arr =  []
        for movie in movies:
            movie_id_arr.append(movie.pk)
        for user in users:
            user_id_arr.append(user.pk)
        N = len(users)
        M = len(movies)
        origin = user_id_arr.index(request.user.pk)
        user_pick = [0] *M 
        #선호 영화에서 점수 반영
        relation_table = [[0] *M for _ in range(N)]
        """ for preference in preferences:
            n = user_id_arr.index(preference.user_id)
            m = movie_id_arr.index(preference.movie1)
            relation_table[n][m] = 1
            m = movie_id_arr.index(preference.movie2)
            relation_table[n][m] = 1
            m = movie_id_arr.index(preference.movie3)
            relation_table[n][m] = 1
            m = movie_id_arr.index(preference.movie4)
            relation_table[n][m] = 1 """
        #리뷰에서 점수 반영
        for review in reviews:
            n = user_id_arr.index(review.user.pk)
            m = movie_id_arr.index(review.movie.pk)
            relation_table[n][m] = review.rate - review.movie.vote_average
            if n == origin:
                user_pick[m] = 1
        #내적ㄱㄱ
        ratio_table = [0]*N
        for n in range(N):
            temp = 0
            vec1 = 0
            vec2 = 0
            for m in range(M):
                temp += relation_table[n][m]*relation_table[origin][m]
                if user_pick[m]:
                    vec1 += relation_table[n][m]**2
                    vec2 += relation_table[origin][m]**2
            ratio_table[n] = (temp/((vec1**0.5)*(vec2**0.5)))/2 +0.5
        #예상점수 계산(평균 기준)
        predict = [0] * M
        for m in range(M):
            if not relation_table[origin][m]:
                weight_sum = 0
                weight_rating = 0
                for n in range(N):
                    if not user_pick[m]:
                        weight_rating += relation_table[n][m]*ratio_table[n]
                        weight_sum += ratio_table[n]
                if weight_sum:
                    predict[m] = weight_rating/weight_sum
        recommand = []
        for m in range(M):
            if predict[m]>0:
                recommand.append(get_object_or_404(Movie, pk=movie_id_arr[m]))
        serializer = MovieListSerializer(recommand, many=True)
        return Response(serializer.data)


@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def urname(request, unknown):
    if request.method == 'GET':
        all_movies = get_list_or_404(Movie)
        gernes = get_list_or_404(Genre)
        actors = get_list_or_404(Actor)
        directors = get_list_or_404(Director)
        movies = []
        for gerne in gernes:
            if gerne.id == unknown:
               serializer = GerneSerializer(gerne)
               return Response(serializer.data)
        for actor in actors:
            if actor.id == unknown:
               serializer = ActorProfileSerializer(actor)
               return Response(serializer.data)

        for director in directors:
            if director.id == unknown:
               serializer = DirectorProfileSerializer(director)
               return Response(serializer.data)