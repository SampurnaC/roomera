from django import forms
from .models import Property,Room

class PropertyForm(forms.ModelForm):
    class Meta:
        model=Property
        fields=['name','description','address','postcode','is_active']
        
class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['title', 'description', 'rent_price', 'max_occupancy', 'is_available','image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Room Title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Room Description'}),
            'rent_price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Rent Price'}),
            'max_occupancy': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Max Occupancy'}),
            'is_available': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        
class RoomSearchForm(forms.Form):
    postcode=forms.CharField(max_length=100,required=False,label="Post Code")
    min_rent=forms.DecimalField(max_digits=10,decimal_places=2,required=False,label="Min Rent")
    max_rent=forms.DecimalField(max_digits=10,decimal_places=2,required=False,label="Max Rent")
    max_occupancy=forms.IntegerField(required=False,label="Max Occupancy")
