from django.urls import path
from .views import landlord_register,verify_email,landlord_login,landlord_logout, landlord_dashboard,landlord_edit

app_name="landlord_account"

urlpatterns = [
    path('register/', landlord_register, name='landlord_register'),
    path("verify/<uidb64>/<token>/", verify_email, name="verify_email"),
    path('login/', landlord_login, name='landlord_login'),
    path('logout/', landlord_logout, name='landlord_logout'),
    path('<slug:slug>/', landlord_dashboard, name='landlord_dashboard'),
    path('<int:pk>/edit', landlord_edit, name='landlord_edit'),
    
]
