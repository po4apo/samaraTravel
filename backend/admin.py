from django.contrib import admin

from .models import PlaceItem, FeedBack


class PlaceItemAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'routName', 'type', 'description', 'smallDescription', 'locationName', 'locationUrl',
              'picPath']



# Register your models here.
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ['pk', 'place', 'user', 'feedbackText', 'feedbackScore']



admin.site.register(PlaceItem, PlaceItemAdmin)
admin.site.register(FeedBack, FeedBackAdmin)
