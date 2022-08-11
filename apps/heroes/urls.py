from django.urls import path

from . import views

urlpatterns = [
    # Heroes urls
    path('hero-list', views.HeroAPIView.as_view(), name='hero-list'),
    path('<int:pk>/', views.HeroRetrieveAPIView.as_view(), name='heroes-retrieve'),

    # Heroes Categories
    path('categories/', views.HeroCategoriesAPIView.as_view(), name='categories'),
    path('categories/<int:pk>/', views.HeroCategoryRetrieveAPIView.as_view(), name='categories-retrieve'),

    # Heroes Skills
    path('skills/', views.HeroSkillsAPIView.as_view(), name='skills'),
    path('skills/int:pk/', views.HeroSkillsRetrieveAPIView.as_view(), name='skill-retrieve'),
]

