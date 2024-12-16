from django.shortcuts import render, redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from admin_part.models import * 
from user_part.models import *
from admin_part.forms import *
from user_part.forms import *
# import pandas as pd
from django.core.paginator import Paginator


def admin_login_fun(request):   
    if request.user.is_authenticated:
        return redirect('dashboard')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username = username)
        if not user_obj.exists():
            messages.info(request, 'Account not found')
            return redirect('admin_login')
            
        user_obj = authenticate(username=username, password=password)

        if user_obj and user_obj.is_superuser:
            login(request, user_obj)
            messages.info(request, 'Login Successfully!.')
            return redirect('dashboard')
            
        messages.info(request, 'Invalid Password')
        return redirect('admin_login')
        
    return render(request,'admin_login.html')

@login_required(login_url='admin_login')
def dashboard_fun(request):
    airlines_var = Airline.objects.all()
     # Set up pagination
    paginator = Paginator(airlines_var, 12)  # Show 10 flights per page
    
    # Get the current page number from the request
    page_number = request.GET.get('page')
    
    # Get the flights for the current page
    page_obj = paginator.get_page(page_number)

    if not request.user.is_superuser:
        messages.info(request , "Access restricted.Only administrators can view this page.")
        return redirect('admin_login')
    
    return render(request, 'dashboard.html',{'page_obj': page_obj}) #{'airlines_data': airlines_var},



@login_required(login_url='admin_login')
def admin_logout_fun(request):
    logout(request)
    messages.success(request ,'Logout successfully.')
    return redirect('admin_login')
#-------------------------------------------crud for airlines--------------------------------
def add_airlines_fun(request):
    if request.POST:
            form = AirlineForm(request.POST, request.FILES)
            form.save()
            context = {'form':form}
            messages.info(request," Airline Added Successfully")
            return redirect('/admin_part/dashboard/',context)
    else:
        form = AirlineForm()
        context = {'form':form}
        return render(request,'add_airlines.html',context)


SEAT_CLASS = (
    ('economy', 'Economy'),
    ('business', 'Business'),
    ('first', 'First')
)

def edit_airlines(request, id):
    airlines = Airline.objects.get(aid=id)
    if request.POST:
            form = AirlineForm(request.POST,request.FILES,instance = airlines)
            if form.is_valid():
                form.save()
                # context = {'form':form}
                messages.info(request,"Data Edited Successfully")
                return redirect('/admin_part/dashboard/',{'form':form})
    else:
        form = AirlineForm(instance = airlines)
        # context = {'form':form}
        return render(request,'edit_airlines.html',{'form':form})


# delete products
@login_required(login_url='admin_login')
def delete_airlines(request, id):
    airlines = Airline.objects.get(aid=id)
    airlines.delete()
    messages.info(request,"delted successfully")
    return redirect('/admin_part/dashboard/')


#--------------------------------------------- crud operationsfor Airport-----------------------------------------------------

@login_required(login_url='admin_login')
def airport_display(request):
    airport_var = Airport.objects.all()
    paginator = Paginator(airport_var, 10)  # Show 10 flights per page
    
    # Get the current page number from the request
    page_number = request.GET.get('page')
    
    # Get the flights for the current page
    page_obj = paginator.get_page(page_number)

    if not request.user.is_superuser:
        messages.info(request , "Access restricted.Only administrators can view this page.")
        return redirect('admin_login')
    
    return render(request, 'airport_display.html',{'page_obj': page_obj}) #{'airport_data': airport_var}

def add_airports_fun(request):
    if request.POST:
            form = AirportForm(request.POST, request.FILES)
            form.save()
            context = {'form':form}
            messages.info(request,"Airport Added Successfully")
            return redirect('/admin_part/airport_display/',context)
    else:
        form = AirportForm()
        context = {'form':form}
        return render(request,'add_airports.html',context)


def edit_airports(request, id):
    airports = Airport.objects.get(apid=id)
    if request.POST:
            form = AirportForm(request.POST,request.FILES,instance = airports)
            if form.is_valid():
                form.save()
                # context = {'form':form}
                messages.info(request,"Airport Edited Successfully")
                return redirect('/admin_part/airport_display/',{'form':form})
    else:
        form = AirportForm(instance = airports)
        # context = {'form':form}
        return render(request,'edit_airports.html',{'form':form})



# delete airports
@login_required(login_url='admin_login')
def delete_airports(request, id):
    airports = Airport.objects.get(apid=id)
    airports.delete()
    messages.info(request,"delted successfully")
    return redirect('/admin_part/airport_display/')

#----------------------------------------users-------------------------------------------------
@login_required(login_url='admin_login')
def user_display(request):
    user_var = User.objects.all()
    paginator = Paginator(user_var, 10)  # Show 10 flights per page
    
    # Get the current page number from the request
    page_number = request.GET.get('page')
    
    # Get the flights for the current page
    page_obj = paginator.get_page(page_number)

    if not request.user.is_superuser:
        messages.info(request , "Access restricted.Only administrators can view this page.")
        return redirect('admin_login')
    
    return render(request, 'user_display.html',{'page_obj': page_obj}) #{'user_data': user_var}

# delete users
@login_required(login_url='admin_login')
def delete_users(request, id):
    users = User.objects.get(id=id)
    users.delete()
    messages.info(request,"delted successfully")
    return redirect('/admin_part/user_display/')


#------------------------------------crud for flights----------------------------------------------------------/

@login_required(login_url='admin_login')
def flight_display(request):
    flight_var = Flight.objects.all()
    paginator = Paginator(flight_var, 10)  # Show 10 flights per page
    
    # Get the current page number from the request
    page_number = request.GET.get('page')
    
    # Get the flights for the current page
    page_obj = paginator.get_page(page_number)

    if not request.user.is_superuser:
        messages.info(request , "Access restricted.Only administrators can view this page.")
        return redirect('admin_login')
    
    return render(request, 'flight_display.html',{'page_obj': page_obj}) #{'flight_data': flight_var}

 
def add_flights(request):
    if request.POST:
            form = FlightForm(request.POST, request.FILES)
            form.save()
            context = {'form':form}
            messages.info(request,"Data Added Successfully")
            return redirect('/admin_part/flight_display/',context)
    else:
        form = FlightForm()
        context = {'form':form}
        return render(request,'add_flights.html',context)


def edit_flights(request, id):
    flights = Flight.objects.get(fid=id)
    if request.POST:
            form = FlightForm(request.POST,request.FILES,instance = flights)
            if form.is_valid():
                form.save()
                # context = {'form':form}
                messages.info(request,"Flight Edited Successfully")
                return redirect('/admin_part/flight_display/',{'form':form})
    else:
        form = FlightForm(instance = flights)
        # context = {'form':form}
        return render(request,'edit_flights.html',{'form':form})


# delete users
@login_required(login_url='admin_login')
def delete_flights(request, id):
    users = Flight.objects.get(fid=id)
    users.delete()
    messages.info(request,"delted successfully")
    return redirect('/admin_part/flight_display/')

# -------------------------booking display at admin panel----------------------------------
@login_required(login_url='admin_login')
def booking_display(request):
    booking_var = Booking.objects.all()
    paginator = Paginator(booking_var, 10) 
    
    # Get the current page number from the request
    page_number = request.GET.get('page')
    
    # Get the bookings for the current page
    page_obj = paginator.get_page(page_number)

    if not request.user.is_superuser:
        messages.info(request , "Access restricted.Only administrators can view this page.")
        return redirect('admin_login')
    
    return render(request, 'booking_display.html',{'page_obj': page_obj})

# ---------------------contact us messages show at admin panel-------------------------------------


# contact us message display at admin side
@login_required(login_url='admin_login')
def contact_us_display(request):
    contact_us_var = ContactUs.objects.all()
    paginator = Paginator(contact_us_var, 10) 
    
    # Get the current page number from the request
    page_number = request.GET.get('page')
    
    # Get the bookings for the current page
    page_obj = paginator.get_page(page_number)

    if not request.user.is_superuser:
        messages.info(request , "Access restricted.Only administrators can view this page.")
        return redirect('admin_login')
    
    return render(request, 'contact_us_display.html',{'page_obj': page_obj})

# delete users
@login_required(login_url='admin_login')
def delete_contact_us(request, id):
    contactus = ContactUs.objects.get(cid=id)
    contactus.delete()
    messages.info(request,"Message delted successfully")
    return redirect('/admin_part/contact_us_display/')
