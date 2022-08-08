from django.http import JsonResponse, HttpResponse

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, generics, filters
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.news.serializers import (
    PostSerializer, PostCategorySerializer,
    NewsCommentsSerializer, UserCommentsSerializer,
    CreateNewsReplyCommentSerializer, CreateNewsCommentSerializer
)
from apps.news.models import (
    Post, PostCategories, CommentReply, NewsComment, User
)


class PostAPIView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'tag']
    serializer_class = PostSerializer
    search_fields = ["name"]
    queryset = Post.objects.all()

    def post(self, request):
        request_body = request.data
        srz = PostSerializer(data=request_body)
        if srz.is_valid():
            srz.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(srz.errors, status=status.HTTP_400_BAD_REQUEST, )

    @classmethod
    def get_extra_actions(cls):
        return []


class PostRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return Response({'msg': 'post not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = PostSerializer(product, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            product = Post.objects.get(id=pk)
        except Post.DoesNotExist:
            return JsonResponse({'msg': 'post not found'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class PostCategoriesAPIView(generics.ListAPIView):
    serializer_class = PostCategorySerializer
    queryset = PostCategories.objects.all()

    def post(self, request):
        request_body = request.data
        new_heroes_category = PostCategories.objects.create(key_role=request_body['key_news'],
                                                       )
        srz = PostCategorySerializer(new_heroes_category, many=False)
        return Response(srz.data, status=status.HTTP_201_CREATED)


class PostCategoryRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            category = PostCategories.objects.get(id=pk)
        except PostCategories.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = PostCategorySerializer(category, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            category = Post.objects.get(id=pk)
        except PostCategories.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AddNewsReplyComment(generics.CreateAPIView):
    queryset = CommentReply.objects.all()
    serializer_class = CreateNewsReplyCommentSerializer


class UserNewsCommentsView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserCommentsSerializer


class UserNewsCommentsUpdateView(RetrieveUpdateDestroyAPIView):
    queryset = NewsComment.objects.all()
    serializer_class = NewsCommentsSerializer


class AddNewsComment(generics.CreateAPIView):
    queryset = NewsComment.objects.all()
    serializer_class = CreateNewsCommentSerializer


