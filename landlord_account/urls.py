from django.urls import path
from .views import index, landlord_register, landlord_dashboard

app_name="roomera"

urlpatterns = [
    path('', index, name='index'),
    path('register/', landlord_register, name='landlord_register'),
    path('dashboard/', landlord_dashboard, name='landlord_dashboard'),
]
