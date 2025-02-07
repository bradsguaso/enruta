from django.shortcuts import render
from rest_framework import generics
from .models import Tarea
from .serializers import TareaSerializer

# Create your views here.

class TareaListCreate(generics.ListCreateAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class TareaRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer
