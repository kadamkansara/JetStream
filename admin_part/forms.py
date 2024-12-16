from django import forms
from admin_part.models import *
from user_part.models import *

class AirlineForm(forms.ModelForm):
    class Meta:
        model = Airline
        fields = ['airline_name','airline_image','status','date_added']
        widgets = {
        'airline_name':forms.TextInput(attrs = {'class':'form-control','placeholder':'Please enter a airline name'}),
        'airline_image':forms.FileInput(attrs = {'class':'form-control'}),
        'status':forms.Select(attrs = {'class':'form-control'}),
        'date_added':forms.DateInput(attrs = {'class':'form-control'}),


        }

class AirportForm(forms.ModelForm):
    class Meta:
        model = Airport
        fields = ['airport_name','status','date_added']
        widgets = {
        'airport_name':forms.TextInput(attrs = {'class':'form-control','placeholder':'Please enter a Airport name'}),
        'status':forms.Select(attrs = {'class':'form-control'}),
        'date_added':forms.DateInput(attrs = {'class':'form-control'})
        }

class FlightForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['code','airline','from_airport','to_airport','air_craft_code','departure','estimated_arrival','departure_time','arrival_time','business_class_price','economy_class_price','departure_time','arrival_time']
        widgets = {
        'code':forms.TextInput(attrs = {'class':'form-control'}),
        'airline':forms.Select(attrs = {'class':'form-control'}),
        'from_airport':forms.Select(attrs = {'class':'form-control'}),
        'to_airport':forms.Select(attrs = {'class':'form-control'}),
        'air_craft_code':forms.TextInput(attrs = {'class':'form-control'}),
        'departure':forms.DateInput(attrs = {'class':'form-control', 'type': 'date'}),
        'estimated_arrival':forms.TimeInput(attrs = {'class':'form-control', 'type': 'date'}), 
        'departure_time':forms.TimeInput(attrs = {'class':'form-control', 'type': 'time'}), 
        'arrival_time':forms.TimeInput(attrs = {'class':'form-control', 'type': 'time'}),     
        'business_class_price':forms.NumberInput(attrs = {'class':'form-control'}),
        'economy_class_price':forms.NumberInput(attrs = {'class':'form-control'}),

        }
