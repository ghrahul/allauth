from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Country
from .serialzers import CountrySerializer
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
# Create your views here.

class Countrylist(APIView):
    def get(self,request):
        country = Country.objects.all()
        serializer = CountrySerializer(country,many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = CountrySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
        

