from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_pk>/', views.movie_detail, name='movie_detail'),
    path('reviews/', views.review_list, name='review_list'),
    path('movies/<int:movie_pk>/reviews/', views.review_create, name='review_create'),
    path('search/<query>/', views.search, name='search'),
    path('profile/<query>/', views.profile),
]