from django.urls import path
from .views import TareaListCreate, TareaRetrieveUpdateDelete
from .views import BusinessListCreate, BusinessRetrieveUpdateDelete

urlpatterns = [
    path('tareas/', TareaListCreate.as_view(), name='tarea-list-create'),
    path('tareas/<int:pk>/', TareaRetrieveUpdateDelete.as_view(), name='tarea-detail'),
    path('business/', BusinessListCreate.as_view(), name='business-list-create'),
    path('business/<int:pk>/', BusinessRetrieveUpdateDelete.as_view(), name='business-detail'),
]