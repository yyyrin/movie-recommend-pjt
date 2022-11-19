from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    path('community/', views.community_list),
    path('community/<int:community_pk>/', views.community_detail),
    path('community/<int:community_pk>/article/<int:article_pk>/', views.article_detail),
    path('community/<int:community_pk>/article/<int:article_pk>/like/', views.article_like),
    path('community/<int:community_pk>/article/<int:article_pk>/comments/', views.comment_create),
    path('community/<int:community_pk>/article/<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail),
    path('community/<int:community_pk>/article/', views.article_create),
    
]