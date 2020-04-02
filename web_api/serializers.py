from rest_framework import serializers, status

from .models import menu, banner, home_body, footer, homeapi


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = banner
        fields = '__all__'


class menusSerializer(serializers.ModelSerializer):
    # bannerFF = PostSerializer(read_only=True)
    class Meta:
        model = homeapi
        depth = 3
        fields = '__all__'