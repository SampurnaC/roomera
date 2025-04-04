from django.db import models
from landlord_account.models import LandlordProfile

class Property(models.Model):
    landlord = models.ForeignKey(LandlordProfile, on_delete=models.CASCADE, related_name="properties")
    name=models.CharField(max_length=100)
    description=models.TextField()
    postcode=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    latitude=models.FloatField(null=True, blank=True)
    longitude=models.FloatField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    property=models.ForeignKey(Property, on_delete=models.CASCADE, related_name="rooms")
    title=models.CharField(max_length=100)
    description=models.TextField()
    rent_price=models.DecimalField(max_digits=10, decimal_places=2)
    max_occupancy=models.IntegerField()
    is_available=models.BooleanField(default=True)
    is_featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.property.landlord} {self.title}"

class RoomImage(models.Model):
    room=models.ForeignKey(Room, on_delete=models.CASCADE, related_name="images")
    image=models.ImageField(upload_to="room_images/")
    uploaded_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Image for {self.room.title}"
