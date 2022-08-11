from rest_framework import serializers

from apps.news.models import (
    Post, PostCategories, NewsComment, CommentReply
                              )
from apps.user.models import User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            'images', 'title', 'created_at', 'text', 'tag', 'in_archive', 'category'
        )


class PostCategorySerializer(serializers.ModelSerializer):
    heroes = PostSerializer(many=True)

    class Meta:
        model = PostCategories
        fields = "key_news", "heroes"


class NewsCommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsComment
        fields = (
            'id', 'text', 'created_data', 'comment',
        )


class UserCommentsSerializer(serializers.ModelSerializer):
    user_comments = NewsCommentsSerializer(many=True)

    class Meta:
        model = User
        fields = (
            'user_comments', 'full_name',
        )


class CommentAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'full_name', 'avatar',
        )


class NewsCommentReplySerializer(serializers.ModelSerializer):
    author = CommentAuthorSerializer(read_only=True)

    class Meta:
        model = CommentReply
        fields = (
            'author', 'comment', 'text', 'likes', 'total_likes', 'created',
        )


class CreateNewsCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsComment
        fields = (
            'author', 'text',
        )


class CreateNewsReplyCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentReply
        fields = (
            'author', 'comment', 'text',
        )

