from django.db import models
from datetime import datetime
from django.utils import timezone
from user_part.models import *
from admin_part.models import *
# Create your models here.
class Passenger(models.Model):
    # or charfield in pid
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=100,default=None)
    last_name = models.CharField(max_length=100,default=None)
    email = models.EmailField(default=None)
    phone_number = models.CharField(max_length=20,default=None)
    address = models.CharField(max_length=100,default=None)
    passport_number = models.CharField(max_length=100,default=None)
    gender = models.CharField(max_length=50, choices=(('Male','Male'), ('Female','Female')), default = 'Male')
    type = models.CharField(max_length=50, choices=(('1','Business Class'), ('2','Economy')), default = '2')

    class Meta:
        db_table=("Passenger")

    def __str__(self):
        return f"{self.first_name}"



class ContactUs(models.Model):
    # or charfield in pid
    cid = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=100,default=None)
    phone_number = models.CharField(max_length=20,default=None)
    message = models.TextField(max_length=1000,default=None)
    
    class Meta:
        db_table=("ContactUs")

    def __str__(self):
        return f"{self.full_name}"   