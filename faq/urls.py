from django.urls import path
from django.conf.urls import url

from .views import ListAllFaq, entrepreneurFaq, businessFaq, generalFaq

urlpatterns = [
    path('all', ListAllFaq.as_view()),
    path('entrepreneur', entrepreneurFaq.as_view()),
    path('business', businessFaq.as_view()),
    path('general', generalFaq.as_view()),
]
