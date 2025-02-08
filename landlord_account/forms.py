from django import forms
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser, LandlordProfile

class LandlordSignUpForm(UserCreationForm):
    phone=forms.CharField(max_length=15, required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    gender=forms.ChoiceField(choices=CustomUser.GENDER_CHOICES, required=False, widget=forms.Select(attrs={'class':'form-control'}))
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date','class':'form-control'}), required=False)
    address=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), required=False)
    properties_owned=forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), required=False)
    business_name=forms.CharField(max_length=100, required=False,widget=forms.TextInput(attrs={'class':'form-control'}))

    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Password"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}), label="Confirm Password"
    )
    
    class Meta:
        model=CustomUser
        fields=['username','email','password1','password2','phone','gender','date_of_birth','address']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        
    def save(self, commit=True):
        user=super().save(commit=False)
        user.is_landlord=True
        
        if commit:
            user.save()

        return user

class LandlordSignInForm(AuthenticationForm):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your username'}),
        label="Username"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter your password'}),
        label="Password"
    )

    def confirm_login_allowed(self, user):
        if not user.is_landlord:
            raise forms.ValidationError(
                "You do not have permission to log in as a landlord.",
                code='invalid_login',
            )
