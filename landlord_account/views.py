from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LandlordSignUpForm,LandlordSignInForm

def landlord_register(request):
    if request.method=="POST":
        form=LandlordSignUpForm(request.POST)
        if form.is_valid():
            user=form.save()
            login(request, user)
            return redirect('roomera:landlord_dashboard')
    else:
        form=LandlordSignUpForm()

    return render(request, 'landlord_account/landlord_register.html', {'form': form})


def landlord_login(request):
    if request.method=="POST":
        form=LandlordSignInForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            return redirect('roomera:landlord_dashboard')
    else:
        form=LandlordSignInForm()
    return render(request, 'landlord_account/landlord_login.html', {'form': form})


def landlord_dashboard(request):
    return render(request, 'landlord_account/landlord_dashboard.html')
