from django import forms
from user_part.models import *
from django.db import models
# from datetime import datetime , timedelta
# Create your models here.
from admin_part.models import *
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


class PassengerForm(forms.ModelForm):
    class Meta:
        model = Passenger
        fields = ['first_name','last_name','email','phone_number','address','passport_number','gender','type']
        widgets = {
        'first_name':forms.TextInput(attrs = {'class':'form-control'}),
        'last_name':forms.TextInput(attrs = {'class':'form-control'}),
        'email':forms.EmailInput(attrs = {'class':'form-control'}),
        'phone_number':forms.TextInput(attrs = {'class':'form-control'}),
        'address':forms.TextInput(attrs = {'class':'form-control'}),
        'passport_number':forms.TextInput(attrs = {'class':'form-control'}),
        'gender':forms.Select(attrs = {'class':'form-control'}),  
        'type':forms.Select(attrs = {'class':'form-control'}) 
  
        }



class SearchFlightsForm(forms.ModelForm):
    class Meta:
        model = Flight
        fields = ['from_airport','to_airport','departure']
        widgets = {
        'from_airport':forms.Select(attrs = {'class':'form-control'}),
        'to_airport':forms.Select(attrs = {'class':'form-control'}),
        'departure':forms.DateInput(attrs = {'class':'form-control','type': 'date'})      
        }

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = "__all__"