from django.db import models
# from datetime import datetime , timedelta
from user_part.models import *
# Create your models here.
from admin_part.models import *
from django.contrib.auth.models import User
from datetime import datetime
from django.utils import timezone


class Airline(models.Model):
    # or charfield in aid
    aid = models.AutoField(primary_key=True)
    airline_name = models.CharField(max_length=100)
    airline_image = models.ImageField(upload_to='images/')
    status = models.CharField(max_length=2, choices=(('1','Active'), ('2','Inactive')), default = 1)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    class Meta:
        db_table=("Airline")

    def __str__(self):
        return f"{self.airline_name}"    




class Airport(models.Model):
    apid = models.AutoField(primary_key=True)
    airport_name = models.CharField(max_length=100,default='coming soon...')
    status = models.CharField(max_length=2, choices=(('1','Active'), ('2','Inactive')), default = 1)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True)

    def __str__(self):
        return str(f"{self.airport_name }")

class Flight(models.Model):
    fid = models.AutoField(primary_key=True)
    code = models.CharField(max_length=250,default=0) #flight code
    airline = models.ForeignKey(Airline, on_delete=models.CASCADE,related_name='airlines',default=1)
    from_airport = models.ForeignKey(Airport , on_delete=models.CASCADE,related_name='from_airport',default=1)
    to_airport = models.ForeignKey(Airport , on_delete=models.CASCADE,related_name='to_airport',default=1)
    air_craft_code = models.CharField(max_length=250,default=0) #airplane code
    departure = models.DateField(null=True)
    estimated_arrival = models.DateField(null=True) 
    departure_time = models.TimeField(null=True)  # New field
    arrival_time = models.TimeField(null=True)    # New field  
    business_class_price = models.FloatField(default=0)
    economy_class_price = models.FloatField(default=0)
    delete_flag = models.IntegerField(default = 0)
    date_added = models.DateTimeField(default = timezone.now)
    date_created = models.DateTimeField(auto_now = True) 

    def __str__(self):
        return str(f"{self.code} [{self.from_airport} , {self.to_airport}]")



class Booking(models.Model):
    flight = models.ForeignKey(Flight, on_delete=models.CASCADE)
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=10, choices=[
        ('economy', 'Economy'),
        ('business', 'Business'),
    ])
    payment_status = models.CharField(max_length=10, choices=[
        ('pending', 'Pending'),
        ('paid', 'Paid'),
        ('cancelled', 'Cancelled'),
    ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.passenger.first_name} {self.passenger.last_name}"
