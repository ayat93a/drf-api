from django.urls import path
from Shows.api.viewsets import ShowListCreateAPIView ,ShowRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('list' , ShowListCreateAPIView.as_view() , name = 'list'),
    path('<int:pk>' , ShowRetrieveUpdateDestroyAPIView.as_view(), name='detail')
]