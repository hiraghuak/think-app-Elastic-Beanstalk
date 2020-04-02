from django.urls import path, include
from .views import contactusView, subscribeView

urlpatterns = [
    path('contactus', contactusView.as_view()),
    path('subscribe_email', subscribeView.as_view())
]
