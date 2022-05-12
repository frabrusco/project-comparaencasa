from django import forms
from .models import Car

class CarsForm(forms.ModelForm):
    
    car_plate = forms.CharField(label='Nombre',
        required=True,
        widget=forms.TextInput(
            attrs = {'class':'form-control',
                    'id': "carPlate",
                    'placeholder': 'search your car plate',
                    }
        )
    )

    class Meta:
        model = Car
        fields = ['car_plate']
