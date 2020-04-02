from rest_framework import serializers
from .models import Cryptocurrency


class CryptocurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Cryptocurrency
        fields = ['id','cryptocurrency', 'price', 'market_cap', 'change']