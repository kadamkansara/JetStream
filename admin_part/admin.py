from django.contrib import admin
from user_part.models import *
from admin_part.models import *

# Register your models here.
#user side 
admin.site.register(Passenger)
admin.site.register(ContactUs)

# admin side
admin.site.register(Airline)
admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Booking)
