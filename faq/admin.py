from django.contrib import admin

# Register your models here.
from .models import generalmodel, businessmodel, entrepreneurmodel, faqresultmodel

admin.site.register(faqresultmodel)
admin.site.register(generalmodel)
admin.site.register(businessmodel)
admin.site.register(entrepreneurmodel)

