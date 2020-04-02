from django.contrib import admin

# Register your models here.
from .models import menu, banner, home_body, footer, homeapi

admin.site.register(menu)
admin.site.register(banner)
admin.site.register(home_body)
admin.site.register(footer)
admin.site.register(homeapi)