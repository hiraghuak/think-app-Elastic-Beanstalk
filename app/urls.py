from django.contrib import admin
from user import views
from django.urls import path, include
from django.conf.urls import url
from django.views.generic import TemplateView, RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('rest_auth/', include('rest_auth.urls')),
    path('api/user/', include('user.urls')),
    path('blog/', include('blog.urls')),
    path('faq/', include('faq.urls')),
    path('web_api/', include('web_api.urls')),
    path('email/', include('contactus.urls')),
]
