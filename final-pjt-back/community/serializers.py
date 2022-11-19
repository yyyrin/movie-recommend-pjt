from rest_framework import serializers
from .models import Community, Article, Comment
from django.contrib.auth import get_user_model

class CommunityListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Community
        fields = '__all__'
        read_only_fields = ('user')

class ArtcleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('community')

class CommuntiySerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')
    article_set = ArtcleSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Community
        fields = '__all__'