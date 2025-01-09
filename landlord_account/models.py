from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    is_landlord = models.BooleanField(default=False)
    phone=models.CharField(max_length=15, blank=True, null=True)
    GENDER_CHOICES=[
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender=models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True, null=True)
    date_of_birth=models.DateField(blank=True, null=True)
    address=models.TextField(blank=True, null=True)
    
    def __str__(self):
        return self.username

class LandlordProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="landlord_profile")
    properties_owned = models.TextField(blank=True, null=True)
    business_name = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username}'s Landlord Profile"

class Property(models.Model):
    landlord = models.ForeignKey(LandlordProfile, on_delete=models.CASCADE, related_name="properties")
    name=models.CharField(max_length=100)
    description=models.TextField()
    address=models.TextField()
    city=models.CharField(max_length=100)
    is_active=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class Room(models.Model):
    property=models.ForeignKey(Property, on_delete=models.CASCADE, related_name="rooms"),
    title=models.CharField(max_length=100)
    description=models.TextField()
    rent_price=models.DecimalField(max_digits=10, decimal_places=2)
    max_occupancy=models.IntegerField()
    is_available=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.title} - {self.property.name}"

