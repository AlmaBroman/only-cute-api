from django.urls import path
from saved_posts import views

urlpatterns = [
    path('saved_posts/', views.SavedPostList.as_view()),
    path('saved_posts/<int:pk>/', views.SavedPostDetail.as_view()),
]
