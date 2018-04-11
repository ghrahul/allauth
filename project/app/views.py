from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Country
from .serialzers import CountrySerializer
# Create your views here.

class Countrylist(APIView):
    def get(self,request):
        country = Country.objects.all()
        serializer = CountrySerializer(country,many=True)
        return Response(serializer.data)
    
        
