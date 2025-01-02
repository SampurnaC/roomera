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
    date_of_birth=models.DateField(blank=True, null=True),
    address=models.TextField(blank=True, null=True),
    
    def __str__(self):
        return self.username

class LandlordProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name="landlord_profile")
    properties_owned = models.TextField(blank=True, null=True)
    business_name = models.CharField(max_length=100, blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.user.username}'s Landlord Profile"
