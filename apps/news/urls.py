from django.urls import path

from .views import PostAPIView, PostCategoriesAPIView, PostRetrieveAPIView, PostCategoryRetrieveAPIView

urlpatterns = [
    path('', PostAPIView.as_view()),
    path('<int:pk>/', PostRetrieveAPIView.as_view()),
    path('categories/', PostCategoriesAPIView.as_view()),
    path('categories/<int:pk>/', PostCategoryRetrieveAPIView.as_view()),
]
