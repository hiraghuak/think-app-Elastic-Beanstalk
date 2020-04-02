from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import render

from .models import  menu, banner, home_body, footer, homeapi


from .serializers import menusSerializer, PostSerializer


class uploadImg(APIView):
    """ List all snippets, or create a new snippet. """

    def get(self, request, format=None):
        snippets = banner.objects.all()
        serializer = PostSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListMenuView(generics.ListAPIView):
    """ Provides a get method handler """
    queryset = homeapi.objects.all()
    serializer_class = menusSerializer
