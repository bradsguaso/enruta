from django.urls import path
from .views import TareaListCreate, TareaRetrieveUpdateDelete

urlpatterns = [
    path('tareas/', TareaListCreate.as_view(), name='tarea-list-create'),
    path('tareas/<int:pk>/', TareaRetrieveUpdateDelete.as_view(), name='tarea-detail'),
]