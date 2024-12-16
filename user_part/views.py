# import stripe
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from admin_part.models import *
from user_part.models import *
from admin_part.forms import *
from user_part.forms import *
import os
import qrcode
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.conf import settings

# Create your views here.
    

def index_fun(request):   
    airlines_var = Airline.objects.all()
    return render(request,'index.html',{'airlines_data': airlines_var})


@login_required(login_url='login')
def contact(request):
    if not request.user.is_superuser and request.user.is_superuser:
        messages.info(request , "Access restricted.Only users and administrator can view this page.")
        return redirect('login')

    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        phone_number = request.POST.get('phone_number')
        message = request.POST.get('message')

        # Save the data to the database
        ContactUs.objects.create(full_name=full_name, phone_number=phone_number, message=message)

        return redirect('/user_part/MessageSentSuccessfully')  # Redirect to a success page


    return render(request, 'contact.html')


def MessageSentSuccessfully(request):
    if not request.user.is_superuser and request.user.is_superuser:
        messages.info(request , "Access restricted.Only users and administrator can view this page.")
        return redirect('login')

    return render(request,'MessageSentSuccessfully.html')

@login_required(login_url='login')
def home_fun(request):
    airlines_var = Airline.objects.all()  
    if not request.user.is_superuser and request.user.is_superuser:
        messages.info(request , "Access restricted.Only users and administrator can view this page.")
        return redirect('login')
    return render(request,'home.html',{'airlines_data': airlines_var})

@login_required(login_url='login')
def profile(request):
    if not request.user.is_superuser and request.user.is_superuser:
        messages.info(request , "Access restricted.Only users and administrator can view this page.")
        return redirect('login')

    return render(request,'profile.html')


def register_fun(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username, email=email, password=password)
        user.save()
        messages.info(request, 'Register Successfully!.')
        return redirect('login')
    
    return render(request, 'register.html')

def login_fun(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, 'Login Successfully!.')
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password!.')
            return render(request, 'login.html')

        
    return render(request, 'login.html')

@login_required(login_url='login')
def logout_fun(request):
    logout(request)
    messages.info(request, 'Logout Successfully!.')
    return redirect('login')

@login_required(login_url='login')
def flights_search(request):
    if not request.user.is_superuser and request.user.is_superuser:
        messages.info(request , "Access restricted.Only users and administrator can view this page.")
        return redirect('login')

    form = SearchFlightsForm()
    if request.method == 'POST':
        form = SearchFlightsForm(request.POST)
        if form.is_valid():
            from_airport = form.cleaned_data['from_airport']
            to_airport = form.cleaned_data['to_airport']
            departure = form.cleaned_data['departure']
           

            flights = Flight.objects.filter(
                from_airport=from_airport,
                to_airport=to_airport,
                departure=departure,
                
                )

            context = {'flights':flights, 'form':form}
            return render(request,'flights_search_result.html',context)
    context = {'form':form}
    return render(request,'flights_search.html',context)


@login_required(login_url='login')
def booking(request,flight_id):

    if not request.user.is_superuser and request.user.is_superuser:
        messages.info(request , "Access restricted.Only users and administrator can view this page.")
        return redirect('login')

    flight = Flight.objects.get(fid=flight_id)
    
    if request.method == 'POST':
        form = PassengerForm(request.POST)
        if form.is_valid():
            passenger = form.save(commit=False)
            passenger.flight = flight
            passenger.save()
            
        
            
            # myvar = passenger.flight
             # Store flight and passenger IDs in session
            request.session['flight_id'] = flight.fid
            request.session['passenger_id'] = passenger.id
            
            return redirect('/user_part/booking_success/') #,{'myvar':myvar}
    else:
        form = PassengerForm()
    
    return render(request, 'booking.html', {'form': form, 'flight': flight})


@login_required(login_url='login')
def booking_success(request):
    if not request.user.is_superuser and request.user.is_superuser:
        messages.info(request , "Access restricted.Only users and administrator can view this page.")
        return redirect('login')
        
    flight_id = request.session.get('flight_id')
    passenger_id = request.session.get('passenger_id')

    # Fetch the flight and passenger based on session data
    flight = Flight.objects.get(fid=flight_id) if flight_id else None
    passenger = Passenger.objects.get(id=passenger_id) if passenger_id else None

    if flight and passenger:
        # Create and save the booking instance
        booking = Booking.objects.create(flight=flight, passenger=passenger)
        booking.save()

        # Create QR code for the booking
        qr_data = f"Booking ID: {booking.id}, Flight: {flight.code}, Passenger: {passenger.first_name} {passenger.last_name}"
        
        # Generate the QR code image
        qr = qrcode.make(qr_data)

        # Define the path to save the QR code
        qr_codes_directory = os.path.join(settings.MEDIA_ROOT, 'qr_codes')
        
        # Make sure the directory exists
        if not os.path.exists(qr_codes_directory):
            os.makedirs(qr_codes_directory)

        # Save the QR code as an image file
        qr_code_path = os.path.join(qr_codes_directory, f"booking_{booking.id}.png")
        qr.save(qr_code_path)

        # Pass the relative path to the template
        qr_code_relative_path = f"/media/qr_codes/booking_{booking.id}.png"
        
        context = {
            'flight': flight,
            'passenger': passenger,
            'qr_code_path': qr_code_relative_path,  # This is the relative path
        }
        
         # Check if the user clicked the 'Download PDF' button
        if request.GET.get('download_pdf'):
            # Render HTML content as a string
            html_string = render_to_string('success.html', context)
            
            # Generate PDF from HTML using xhtml2pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename="booking_{booking.id}.pdf"'

            pisa_status = pisa.CreatePDF(html_string, dest=response)
            if pisa_status.err:
                return HttpResponse('Error generating PDF', status=500)
            return response
            

        return render(request, 'success.html', context)
    else:
        return render(request, 'error.html', {'error_message': 'Booking details not found.'})

