from django.shortcuts import render
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from .models import Tarea
from .models import Business
from .models import Charge
from .models import Request
from .models import TransportWorker
from .models import User
from .serializers import TareaSerializer
from .serializers import BusinessSerializer
from .serializers import ChargeSerializer
from .serializers import RequestSerializer
from .serializers import TransportWorkerSerializer
from .serializers import UserSerializer


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

class ChargeListCreate(generics.ListCreateAPIView):
    queryset = Charge.objects.all()
    serializer_class = ChargeSerializer

class ChargeRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Charge.objects.all()
    serializer_class = ChargeSerializer

class RequestListCreate(generics.ListCreateAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer
    pagination_class = pagination_class = PageNumberPagination

class RequestRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Request.objects.all()
    serializer_class = RequestSerializer

class TransportWorkerListCreate(generics.ListCreateAPIView):
    queryset = TransportWorker.objects.all()
    serializer_class = TransportWorkerSerializer

class TransportWorkerRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = TransportWorker.objects.all()
    serializer_class = TransportWorkerSerializer

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = TransportWorkerSerializer

class UserRetrieveUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return Response(serializer.data)

