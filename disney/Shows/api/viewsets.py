from rest_framework.generics import ListCreateAPIView , RetrieveUpdateDestroyAPIView

from Shows.models import Show
from .serializers import Showserializers
from .permissions import ISOwnerOrReader 
from rest_framework.permissions import IsAuthenticated



class ShowListCreateAPIView(ListCreateAPIView):
    serializer_class = Showserializers
    queryset = Show.objects.all() 



class ShowRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = Showserializers
    queryset = Show.objects.all()
    permission_classes =  (ISOwnerOrReader , IsAuthenticated)