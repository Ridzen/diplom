from django.urls import path

from . import views

urlpatterns = [

    # post urls
    path('posting-news', views.PostAPIView.as_view()),
    path('<int:pk>/', views.PostRetrieveAPIView.as_view()),
    path('categories/', views.PostCategoriesAPIView.as_view()),
    path('categories/<int:pk>/', views.PostCategoryRetrieveAPIView.as_view()),

    # news comments aki post urls
    path('add-news-comment/', views.AddNewsComment.as_view(),
         name='add-news-comment'),
    path('add-news-reply-comment/', views.AddNewsReplyComment.as_view(),
         name='add-news-reply-comment'),
    path('user-profile-comments/<int:pk>/',
         views.UserNewsCommentsView.as_view(), name='user-profile-comments'),
    path('user-profile-comments/update/<int:pk>/',
         views.UserNewsCommentsUpdateView.as_view(), name='user-profile-comments_update'),

]
