from django.contrib import admin
from .models import Property,Room,RoomImage
# Register your models here.
admin.site.register(Property)
admin.site.register(Room)
admin.site.register(RoomImage)
