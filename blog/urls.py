from django.urls import path, include

from .views import mediumblog, TOIBusinessApi, TOITechnologyNewsApi, EntrepreneurApi, ListCryptocurrencyView

urlpatterns = [
    path('our_partner_rss', mediumblog.as_view()),
    path('toi_business_rss', TOIBusinessApi.as_view()),
    path('toi_technology_news_rss', TOITechnologyNewsApi.as_view()),
    path('entrepreneur_rss', EntrepreneurApi.as_view()),
    path('newblog', ListCryptocurrencyView.as_view()),
]
