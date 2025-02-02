from .models import Property

def landlord_properties(request):
    if request.user.is_authenticated and hasattr(request.user, 'landlord_profile'):
        properties = Property.objects.filter(landlord=request.user.landlord_profile)
        return {'properties': properties}  # Makes properties available in all templates
    return {'properties': None}

