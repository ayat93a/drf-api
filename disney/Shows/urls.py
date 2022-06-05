import jwt
from rest_framework_simplejwt import views as jwt_view
from django.urls import path
from Shows.api.viewsets import ShowListCreateAPIView ,ShowRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('list' , ShowListCreateAPIView.as_view() , name = 'list'),
    path('<int:pk>' , ShowRetrieveUpdateDestroyAPIView.as_view(), name='detail'),
    path('token' , jwt_view.TokenObtainPairView.as_view() , name = 'token_obtain'),
    path('refresh' , jwt_view.TokenRefreshView.as_view() , name = 'refresh'),
]

#    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY1NDUxMjQ3NywiaWF0IjoxNjU0NDI2MDc3LCJqdGkiOiI5ZTNmOGVkYjljZjI0ODVlYmNlYjg0OWUxMmQyOGNmNSIsInVzZXJfaWQiOjF9.EY7MvDtPkD9JiHJqQtXC_8i0XRaeojhHfCW_AuUNnhI",
#     "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU0NDI2Mzc3LCJpYXQiOjE2NTQ0MjYwNzcsImp0aSI6ImU4MzU0NDY5M2JkZTQ2ZmQ5ODgyYTIzYTdiY2NiYzMxIiwidXNlcl9pZCI6MX0.dYzM8mD7ArFlIqDxRW_YyjJyE26O5X-MNeXuALOKR10"
