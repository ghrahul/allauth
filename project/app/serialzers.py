from rest_framework import serializers
from .models import Country
from django.contrib.auth.models import User

class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = "__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            'url', 'username', 'email', 'password'
        ]

        extra_kwargs = {
            "password": {"write_only": True},
        }
        



     