from rest_framework import generics
from rest_framework import filters
from rest_framework import viewsets

from .serializers import faqresultSerializer, entrepreneurSerializer, businessSerializer, generalSerializer
from faq import models


class ListAllFaq(generics.ListCreateAPIView):
    """ List All Faq View """
    queryset = models.faqresultmodel.objects.all()
    serializer_class = faqresultSerializer
    filter_backends = [filters.SearchFilter]
    # search_fields = []


class entrepreneurFaq(generics.ListCreateAPIView):
    """ entrepreneur View """
    queryset = models.entrepreneurmodel.objects.all()
    serializer_class = entrepreneurSerializer


class businessFaq(generics.ListCreateAPIView):
    """ business View """
    queryset = models.businessmodel.objects.all()
    serializer_class = businessSerializer


class generalFaq(generics.ListCreateAPIView):
    """ general View """
    queryset = models.generalmodel.objects.all()
    serializer_class = generalSerializer

