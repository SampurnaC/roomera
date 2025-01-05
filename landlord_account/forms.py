from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, LandlordProfile

class LandlordSignUpForm(UserCreationForm):
    phone=forms.CharField(max_length=15, required=False)
    gender=forms.ChoiceField(choices=CustomUser.GENDER_CHOICES, required=False)
    date_of_birth = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), required=False)
    address=forms.CharField(widget=forms.Textarea, required=False)
    properties_owned=forms.CharField(widget=forms.Textarea, required=False)
    business_name=forms.CharField(max_length=100, required=False)

    class Meta:
        model=CustomUser
        fields=['username','email','password1','password2','phone','gender','date_of_birth','address']
        
    def save(self, commit=True):
        user=super().save(commit=False)
        user.is_landlord=True
        
        if commit:
            user.save()

        LandlordProfile.objects.create(
            user=user,
            properties_owned=self.cleaned_data.get('properties_owned'),
            business_name=self.cleaned_data.get('business_name')
        )
        
        return user
