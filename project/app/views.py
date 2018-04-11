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
from django.http import Http404
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
    
  
class CountryDetail(APIView):
    def get_object(self,pk):
        try:
            return Country.objects.get(pk=pk)
        except Country.DoesNotExist:
            raise  Http404
        
    def get(self, request, pk, format=None):
         countrypk = self.get_object(pk)
         serializer = CountrySerializer(countrypk)
         return Response(serializer.data)

    def put(self, request, pk, format=None):
        countrypk = self.get_object(pk)
        serializer = CountrySerializer(countrypk, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        countrypk = self.get_object(pk)
        countrypk.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
           

        


            
    

    
        

