from django.urls import path
from .views import index,add_property,add_room,search_rooms

app_name="landlord_property"

urlpatterns = [
    path('', index, name='home'),
    path('rooms/search/', search_rooms, name='search_rooms'),
    path('property/add/', add_property, name='add_property'),
    path('property/<int:property_id>/add-room', add_room, name='add_room'),
]
