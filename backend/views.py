from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import PlaceItem, FeedBack
from .serializer import PlaceItemSerializer, FeedBackSerializer, UserSerializer


# Create your views here.
class PlaceItemViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = PlaceItem.objects.all()
    serializer_class = PlaceItemSerializer


class FeedBackViewSet(ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer