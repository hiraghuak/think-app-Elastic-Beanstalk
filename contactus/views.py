from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models import contactus
from .serializers import contactusSerializer, subscribeSerializer


class contactusView(APIView):
    """ contactus view """

    def post(self, request, format=None):
        serializer = contactusSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class subscribeView(APIView):
    """ subscribe View """

    def post(self, request, format=None):
        serializer = subscribeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("sucessfully subscribed email", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
