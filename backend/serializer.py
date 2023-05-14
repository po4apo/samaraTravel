from django.contrib.auth.models import User
from rest_framework import serializers

from .models import PlaceItem, FeedBack


class PlaceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceItem
        fields = ['pk', 'name', 'routName', 'type', 'description', 'smallDescription', 'locationName', 'locationUrl',
                  'picPath']
        depth = 2


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['pk', 'first_name', 'last_name']


class PlaceItemSerializerForFeedBack(serializers.ModelSerializer):
    class Meta:
        model = PlaceItem
        fields = ['pk']
        depth = 2


class FeedBackSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    place = PlaceItemSerializerForFeedBack(read_only=True)

    class Meta:
        model = FeedBack
        fields = ['pk', 'place', 'user', 'feedbackText', 'feedbackScore']
        depth = 2
