from rest_framework import serializers
from .models import Community, Article, Comment
from django.contrib.auth import get_user_model

class CommunityListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Community
        fields = '__all__'
        read_only_fields = ('user',)


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article','user',)


class ArticleSerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')
    comment_set = CommentSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)
    community = CommunityListSerializer(read_only= True)
    like_users = UserSerializer(many=True, read_only=True)
    class Meta:
        model = Article
        fields = '__all__'


class CommuntiySerializer(serializers.ModelSerializer):
    class UserSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('pk', 'username')
    article_set = ArticleSerializer(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Community
        fields = '__all__'
