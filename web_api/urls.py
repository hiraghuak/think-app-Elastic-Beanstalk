from django.urls import path, include
from .views import ListMenuView, uploadImg

urlpatterns = [
    path('homepage', ListMenuView.as_view()),
    path('imguploda', uploadImg.as_view()),
]
