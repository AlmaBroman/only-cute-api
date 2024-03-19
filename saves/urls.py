from django.urls import path
from likes import views

urlpatterns = [
    path('saves/', views.LikeList.as_view()),
    path('saves/<int:pk>/', views.LikeDetail.as_view()),
]