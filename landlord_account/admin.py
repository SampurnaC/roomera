from django.contrib import admin

from . models import CustomUser, LandlordProfile

admin.site.register(CustomUser)
admin.site.register(LandlordProfile)
