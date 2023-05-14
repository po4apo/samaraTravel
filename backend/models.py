from django.db import models
from django.contrib.auth.models import User


class PlaceItem(models.Model):
    name = models.CharField(max_length=256)
    routName = models.CharField(max_length=256)
    type = models.CharField(max_length=256)
    description = models.CharField(max_length=256)
    smallDescription = models.CharField(max_length=256)
    locationName = models.CharField(max_length=256)
    locationUrl = models.URLField()
    picPath = models.URLField()

    def __str__(self):
        return self.name


class FeedBack(models.Model):
    place = models.ForeignKey(PlaceItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    feedbackText = models.CharField(max_length=256)
    feedbackScore = models.CharField(max_length=256)

    def __str__(self):
        return self.feedbackText


