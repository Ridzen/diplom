from django.urls import path

from .views import (
    HeroesAPIView, HeroesCategoriesAPIView,
    HeroesSkillsAPIView, HeroesRetrieveAPIView,
    HeroesCategoryRetrieveAPIView, HeroesSkillsRetrieveAPIView,
)
urlpatterns = [
    path('', HeroesAPIView.as_view()),
    path('<int:pk>/', HeroesRetrieveAPIView.as_view()),
    path('categories/', HeroesCategoriesAPIView.as_view()),
    path('categories/<int:pk>/', HeroesCategoryRetrieveAPIView.as_view()),
    path('skills/', HeroesSkillsAPIView.as_view()),
    path('skills/int:pk/', HeroesSkillsRetrieveAPIView.as_view())
]

