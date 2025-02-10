from django.shortcuts import render
from rest_framework import generics
from .models import Tarea
from .models import Business
from .serializers import TareaSerializer
from .serializers import BusinessSerializer

# Create your views here.

class TareaListCreate(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class TareaRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class BusinessListCreate(generics.ListCreateAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer

class BusinessRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Business.objects.all()
    serializer_class = BusinessSerializer