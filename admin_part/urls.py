from django.conf import settings
from django.urls import path
from django.conf.urls.static import static
from admin_part.views import *
from user_part.views import *


urlpatterns = [
    # path('',,name=''),
    # admin-->
    path('admin_login/',admin_login_fun,name="admin_login"),
    path('dashboard/',dashboard_fun,name="dashboard"), 
    path('admin_logout/',admin_logout_fun, name="admin_logout"),

    
    # crud for airlines
    path('add_airlines/',add_airlines_fun, name="add_airlines"),
    path('edit_airlines/<int:id>',edit_airlines,name = 'edit_airlines'),
    path('delete_airlines/<int:id>',delete_airlines,name = 'delete_airlines'),

    
    # crud operations for places 
    path('airport_display/',airport_display,name="airport_display"),
    path('add_airports/',add_airports_fun, name="add_airports"),
    path('edit_airports/<int:id>',edit_airports,name = 'edit_airports'),
    path('delete_airports/<int:id>',delete_airports,name = 'delete_airports'),

    # crud for users
    path('user_display/',user_display,name="user_display"),
    path('delete_users/<int:id>',delete_users,name = 'delete_users'),

    # crud for flights
    path('flight_display/',flight_display,name="flight_display"),
    path('add_flights/',add_flights, name="add_flights"),
    path('edit_flights/<int:id>',edit_flights,name = 'edit_flights'),
    path('delete_flights/<int:id>',delete_flights,name = 'delete_flights'),


    #crud for passenger bookings
    path('booking_display/',booking_display,name="booking_display"),


    # contact us messages display
    path('contact_us_display/',contact_us_display,name="contact_us_display"),
    path('delete_contact_us/<int:id>',delete_contact_us,name="delete_contact_us"),

    
   ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)