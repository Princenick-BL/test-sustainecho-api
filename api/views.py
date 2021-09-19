from django.shortcuts import render
from rest_framework import generics
from .serializer import EmployeeSerializer,VilleSerializer,PaysSerializer,MarqueSerializer
from .models import Employés,Pays,Ville,Marques
# Create your views here.

class PaysView(generics.ListAPIView):
    queryset= Pays.objects.all()
    serializer_class = PaysSerializer

class VilleView(generics.ListAPIView):
    queryset= Ville.objects.all()
    serializer_class = VilleSerializer

class MarqueView(generics.ListAPIView):
    queryset= Marques.objects.all()
    serializer_class = MarqueSerializer

class EmployeeView(generics.ListAPIView):
    queryset= Employés.objects.all()
    serializer_class = EmployeeSerializer


