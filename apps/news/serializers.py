from rest_framework import serializers

from apps.news.models import Post, PostCategories


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'



class PostCategorySerializer(serializers.ModelSerializer):
    heroes = PostSerializer(many=True)

    class Meta:
        model = PostCategories
        fields = "__all__"

