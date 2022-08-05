from django.http import JsonResponse, HttpResponse

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import status, generics, filters
from rest_framework.views import APIView
from rest_framework.response import Response

from apps.heroes.models import Heroes, HeroesCategories, HeroesSkills
from apps.heroes.serializers import HeroesSerializer, HeroesSkillsSerializer, HeroesCategorySerializer


class HeroesAPIView(generics.ListCreateAPIView):
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['role']
    serializer_class = HeroesSerializer
    search_fields = ["name"]
    queryset = Heroes.objects.all()

    def post(self, request):
        request_body = request.data
        srz = HeroesSerializer(data=request_body)
        if srz.is_valid():
            srz.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(srz.errors, status=status.HTTP_400_BAD_REQUEST, )

    @classmethod
    def get_extra_actions(cls):
        return []


class HeroesRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            product = Heroes.objects.get(id=pk)
        except Heroes.DoesNotExist:
            return Response({'msg': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = HeroesSerializer(product, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            product = Heroes.objects.get(id=pk)
        except Heroes.DoesNotExist:
            return JsonResponse({'msg': 'product not found'}, status=status.HTTP_404_NOT_FOUND)
        product.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)


class HeroesCategoriesAPIView(generics.ListAPIView):
    serializer_class = HeroesCategorySerializer
    queryset = HeroesCategories.objects.all()

    def post(self, request):
        request_body = request.data
        new_heroes_category = HeroesCategories.objects.create(key_role=request_body['key_role'],
                                                       )
        srz = HeroesCategorySerializer(new_heroes_category, many=False)
        return Response(srz.data, status=status.HTTP_201_CREATED)


class HeroesCategoryRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            category = HeroesCategories.objects.get(id=pk)
        except HeroesCategories.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = HeroesCategorySerializer(category, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            category = Heroes.objects.get(id=pk)
        except HeroesCategories.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HeroesSkillsAPIView(generics.ListAPIView):
    serializer_class = HeroesSkillsSerializer
    queryset = HeroesSkills.objects.all()

    def post(self, request):
        request_body = request.data
        new_heroes_skills = HeroesSkills.objects.create(first_skill=request_body['first_skill'],
                                                       )
        srz = HeroesSkillsSerializer(new_heroes_skills, many=False)
        return Response(srz.data, status=status.HTTP_201_CREATED)


class HeroesSkillsRetrieveAPIView(APIView):
    def get(self, request, pk):
        try:
            skill = HeroesSkills.objects.get(id=pk)
        except HeroesSkills.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        srz = HeroesSkillsSerializer(skill, many=False)
        return Response(srz.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        try:
            skill = Heroes.objects.get(id=pk)
        except HeroesSkills.DoesNotExist:
            return Response({'msg': 'category not found'}, status=status.HTTP_404_NOT_FOUND)
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)