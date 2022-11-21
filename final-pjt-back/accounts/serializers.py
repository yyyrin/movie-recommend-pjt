from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer
from django.contrib.auth import get_user_model
from community.serializers import ArticleSerializer
from movies.serializers import ReviewSerializer
from movies.models import Review
from community.models import Article
from .models import Profile
class UserSerializer(RegisterSerializer):

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        return data

class ImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = '__all__'
        read_only_fields = ('username', 'password')

class ProfileSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = '__all__'
    user = UserSerializer(read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)
    articles = ArticleSerializer(many=True, read_only=True)

    class Meta:
        model = Profile
        fields = '__all__'