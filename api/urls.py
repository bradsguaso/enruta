from django.urls import path
from .views import TareaListCreate, TareaRetrieveUpdateDelete
from .views import BusinessListCreate, BusinessRetrieveUpdateDelete
from .views import ChargeListCreate, ChargeRetrieveUpdateDelete
from .views import RequestListCreate, RequestRetrieveUpdateDelete
from .views import TransportWorkerListCreate, TransportWorkerRetrieveUpdateDelete
from .views import UserListCreate, UserRetrieveUpdateDelete
from .views import UserProfileView

urlpatterns = [
    path('tareas/', TareaListCreate.as_view(), name='tarea-list-create'),
    path('tareas/<int:pk>/', TareaRetrieveUpdateDelete.as_view(), name='tarea-detail'),
    path('business/', BusinessListCreate.as_view(), name='business-list-create'),
    path('business/<int:pk>/', BusinessRetrieveUpdateDelete.as_view(), name='business-detail'),
    path('charges/', ChargeListCreate.as_view(), name='charge-list-create'),
    path('charges/<int:pk>/', ChargeRetrieveUpdateDelete.as_view(), name='charge-detail'),
    path('requests/', RequestListCreate.as_view(), name='request-list-create'),
    path('requests/<int:pk>/', RequestRetrieveUpdateDelete.as_view(), name='request-detail'),
    path('transportworkers/', TransportWorkerListCreate.as_view(), name='transportworker-list-create'),
    path('transportworkers/<int:pk>/', TransportWorkerRetrieveUpdateDelete.as_view(), name='transportworker-detail'),
    path('users/', UserListCreate.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDelete.as_view(), name='user-detail'),
    path('profile/', UserProfileView.as_view(), name='user_profile'),
]