from django.shortcuts import render,redirect,get_object_or_404
from .forms import PropertyForm,RoomForm,RoomSearchForm
from landlord_account.models import LandlordProfile
from .models import Property,Room
from django.contrib.auth.decorators import login_required

def index(request):
    featured_rooms = Room.objects.filter(is_featured=True)
    return render(request, 'landlord_property/index.html',{'featured_rooms': featured_rooms})

@login_required
def add_property(request):
    if not request.user.is_landlord:
        return redirect('home')
    try:
        landlord_profile = request.user.landlord_profile
    except LandlordProfile.DoesNotExist:
        return redirect('home')

    if request.method=="POST":
        form=PropertyForm(request.POST)
        property=form.save(commit=False)
        property.landlord=landlord_profile
        property.save()
        
        return redirect('landlord_property:home')
    else:
        form=PropertyForm()
    return render(request,'landlord_property/add_property.html',{'form': form})

@login_required
def add_room(request,property_id):
    if not request.user.is_landlord:
        return redirect("landlord_property:home")
    property_obj=get_object_or_404(Property,id=property_id,landlord=request.user.landlord_profile)
    
    if request.method=="POST":
        form=RoomForm(request.POST)
        room=form.save(commit=False)
        room.property=property_obj
        room.save()
        return redirect('landlord_property:home')
    else:
        form=RoomForm()
        
    return render(request,'landlord_property/add_room.html',{'form': form, 'property_id': property_id})

def search_rooms(request):
    form=RoomSearchForm(request.GET or None)
    rooms=None
    if request.GET:
        rooms=Room.objects.filter(is_available=True)
    
    if form.is_valid():
        postcode=form.cleaned_data.get("postcode")
        min_rent=form.cleaned_data.get("min_rent")
        max_rent=form.cleaned_data.get("max_rent")
        max_occupancy=form.cleaned_data.get("max_occupancy")
        
        if postcode:
            rooms=rooms.filter(property__postcode__icontains=postcode)
        if min_rent is not None:
            rooms=rooms.filter(rent_price__gte=min_rent)
        if max_rent is not None:
            rooms=rooms.filter(rent_price__lte=max_rent)
        if max_occupancy is not None:
            rooms=rooms.filter(max_occupancy__lte=max_occupancy)
        
    return render(request, "landlord_property/search_results.html", {'form':form,'rooms':rooms})

def room_detail(request, room_id):
    room = get_object_or_404(Room, id=room_id)
    return render(request, 'landlord_property/room_detail.html',{'room': room})
