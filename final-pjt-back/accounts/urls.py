from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('profile/<str:username>/', views.profile),
    path('profile/<int:user_pk>/img/', views.img_change),
    path('report/<int:user_pk>/', views.report),

]