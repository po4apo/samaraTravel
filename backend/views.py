from rest_framework.viewsets import ModelViewSet

from .models import PlaceItem, FeedBack
from .serializer import PlaceItemSerializer, FeedBackSerializer


# Create your views here.
class PlaceItemViewSet(ModelViewSet):
    queryset = PlaceItem.objects.all()
    serializer_class = PlaceItemSerializer


class FeedBackViewSet(ModelViewSet):
    queryset = FeedBack.objects.all()
    serializer_class = FeedBackSerializer

