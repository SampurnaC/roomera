from django.urls import path
from .views import landlord_register,landlord_login,landlord_dashboard

app_name="roomera"

urlpatterns = [
    path('register/', landlord_register, name='landlord_register'),
    path('login/', landlord_login, name='landlord_login'),
    path('dashboard/', landlord_dashboard, name='landlord_dashboard'),
]
