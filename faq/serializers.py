from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from faq import models


class entrepreneurSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.entrepreneurmodel
        fields = ('id', 'title', 'description',)


class businessSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.businessmodel
        fields = ('id', 'title', 'description',)


class generalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.generalmodel
        fields = ('id', 'title', 'description')


class faqresultSerializer(ModelSerializer):
    entrepreneur = entrepreneurSerializer(many=True)
    business = businessSerializer(many=True)
    general = generalSerializer(many=True)

    class Meta:
        model = models.faqresultmodel
        fields = '__all__'
