from rest_framework import serializers
from .models import urls


class URLdeSerializer(serializers.ModelSerializer):

    class Meta:
        model = urls
        fields = ['mainURL', 'shortURL']


class URLSerializer(serializers.ModelSerializer):
    URL = serializers.CharField(source='mainURL')

    class Meta:
        model = urls
        fields = ['URL']