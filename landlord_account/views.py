from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, get_user_model
from django.contrib.auth.decorators import login_required
from .forms import LandlordSignUpForm,LandlordSignInForm,UserEditForm,LandlordEditForm
from .email import send_verification_email
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str
from .models import CustomUser, LandlordProfile
from django.contrib import messages
from .tokens import verify_verification_token
from landlord_property.models import Property,Room

User=get_user_model()

def landlord_register(request):
  if request.method=="POST":
    form=LandlordSignUpForm(request.POST)
    if form.is_valid():
        user=form.save(commit=False)
        user.is_verified=False
        user.save()
        
        LandlordProfile.objects.create(
          user=user,
          properties_owned=form.cleaned_data.get('properties_owned'),
          business_name=form.cleaned_data.get('business_name')
        )

        send_verification_email(user, request)
        return redirect('landlord_account:landlord_dashboard', slug=user.slug)
  else:
    form=LandlordSignUpForm()

  return render(request, 'landlord_account/landlord_register.html', {'form': form})

def verify_email(request, uidb64, token):
    user = verify_verification_token(uidb64, token)
    
    if user:
        landlord_profile = LandlordProfile.objects.get(user=user)
        landlord_profile.is_verified = True
        landlord_profile.save()
        
        # login(request, user)
        messages.success(request, "Your email has been verified!")
        return redirect("landlord_account:landlord_login")
    else:
        messages.error(request, "The verification link is invalid or has expired.", extra_tags='danger')
        return redirect("landlord_account:landlord_register")
  
def landlord_login(request):
    if request.method=="POST":
        form=LandlordSignInForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('landlord_account:landlord_dashboard', slug=user.slug)
    else:
        form=LandlordSignInForm()
    return render(request, 'landlord_account/landlord_login.html', {'form': form})

@login_required
def landlord_logout(request):
    logout(request)
    return redirect('landlord_property:home')

@login_required
def landlord_edit(request,pk):
    landlord_profile=get_object_or_404(LandlordProfile, user=request.user)
    
    if request.method=="POST":
        user_form=UserEditForm(request.POST, instance=request.user)
        landlord_profile_form=LandlordEditForm(request.POST, instance=landlord_profile)
        if user_form.is_valid() and landlord_profile_form.is_valid():
            user_form.save()
            landlord_profile_form.save()
            return redirect('landlord_account:landlord_dashboard',pk=landlord_profile.id)
    else:
        user_form=UserEditForm(instance=request.user)
        landlord_profile_form=LandlordEditForm(instance=landlord_profile)  
    return render(request, 'landlord_account/landlord_edit.html',{'user_form': user_form,'landlord_profile_form':landlord_profile_form})

# def landlord_dashboard(request):
#   # Get the landlord profile of the logged-in user
#   landlord_profile = LandlordProfile.objects.get(user=request.user)

#   # Get all properties of the landlord
#   properties = Property.objects.filter(landlord=landlord_profile)

#   # Get all rooms of the landlord (through related properties)
#   rooms = Room.objects.filter(property__landlord=landlord_profile)

#   return render(request, 'landlord_account/landlord_dashboard.html', {
#       'landlord_profile': landlord_profile,
#       'properties': properties,
#       'rooms': rooms
#   })

def landlord_dashboard(request, slug):
    landlord_user=get_object_or_404(CustomUser, slug=slug, is_landlord=True)
    landlord_profile = LandlordProfile.objects.get(user=landlord_user)
    properties = Property.objects.filter(landlord=landlord_profile)
    rooms = []
    for property in properties:
        rooms.extend(Room.objects.filter(property=property))
    
    return render(request, 'landlord_account/landlord_dashboard.html', {
        'landlord_profile': landlord_profile,
        'properties': properties,
        'rooms': rooms
    })
