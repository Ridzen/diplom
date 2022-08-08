from django.urls import path

from . import views

urlpatterns = [
    # Heroes urls
    path('heroes-list', views.HeroesAPIView.as_view(), name='heroes-list'),
    path('<int:pk>/', views.HeroesRetrieveAPIView.as_view(), name='heroes-retrieve'),

    # Heroes Categories
    path('categories/', views.HeroesCategoriesAPIView.as_view(), name='categories'),
    path('categories/<int:pk>/', views.HeroesCategoryRetrieveAPIView.as_view(), name='categories-retrieve'),

    # Heroes Skills
    path('skills/', views.HeroesSkillsAPIView.as_view(), name='skills'),
    path('skills/int:pk/', views.HeroesSkillsRetrieveAPIView.as_view(), name='skill-retrieve'),
]

