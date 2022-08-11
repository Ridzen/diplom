from django.http import JsonResponse, HttpResponse

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.heroes.models import (
    Hero, HeroCategories, HeroSkills
)
from apps.heroes.serializers import (
    HeroSerializer, HeroSkillsSerializer, HeroCategorySerializer
)


class HeroAPIView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['role']
    serializer_class = HeroSerializer
    search_fields = ["name", "role"]
    queryset = Hero.objects.all()

    def post(self, request):
        request_body = request.data
        srz = HeroSerializer(data=request_body)
        if srz.is_valid():
            srz.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(srz.errors, status=status.HTTP_400_BAD_REQUEST, )

    @classmethod
    def get_extra_actions(cls):
        return []


class HeroRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Hero.objects.get(id=pk)
        except Hero.DoesNotExist:
            return Response({'msg': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = HeroSerializer(product, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            product = Hero.objects.get(id=pk)
        except Hero.DoesNotExist:
            return JsonResponse({'msg': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class HeroCategoriesAPIView(generics.ListAPIView):
    serializer_class = HeroCategorySerializer
    queryset = HeroCategories.objects.all()

    def post(self, request):
        request_body = request.data
        new_heroes_category = HeroCategories.objects.create(key_role=request_body['key_role'],
                                                       )
        srz = HeroCategorySerializer(new_heroes_category, many=False)
        return Response(srz.data, status=status.HTTP_201_CREATED)


class HeroCategoryRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            category = HeroCategories.objects.get(id=pk)
        except HeroCategories.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = HeroCategorySerializer(category, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            category = Hero.objects.get(id=pk)
        except HeroCategories.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HeroSkillsAPIView(generics.ListAPIView):
    serializer_class = HeroSkillsSerializer
    queryset = HeroSkills.objects.all()

    def post(self, request):
        request_body = request.data
        new_heroes_skills = HeroSkills.objects.create(first_skill=request_body['first_skill'],
                                                       )
        srz = HeroSkillsSerializer(new_heroes_skills, many=False)
        return Response(srz.data, status=status.HTTP_201_CREATED)


class HeroSkillsRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            skill = HeroSkills.objects.get(id=pk)
        except HeroSkills.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = HeroSkillsSerializer(skill, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            skill = Hero.objects.get(id=pk)
        except HeroSkills.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)