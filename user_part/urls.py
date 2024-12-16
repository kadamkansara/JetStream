from django.conf import settings
from django.conf.urls.static import static

from django.urls import path
from user_part.views import *
from admin_part.views import *

from django.contrib.auth import views as auth_views

urlpatterns = [
    path('index/',index_fun, name='index'),
    path('contact/',contact, name='contact'),
    path('MessageSentSuccessfully/',MessageSentSuccessfully, name='MessageSentSuccessfully'),
    path('home/',home_fun, name='home'),
    path('profile/',profile,name='profile'),
    path('register/',register_fun, name='register'),
    path('login/',login_fun, name='login'),
    path('logout/',logout_fun,name='logout'),

     # reset password
    path('password_reset/',auth_views.PasswordResetView.as_view(template_name='password_reset_form.html'),name='password_reset'),
    path('password_reset_done/',auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),name='password_reset_confirm'),
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),


    path('flights_search/',flights_search, name="flights_search"),
    path('booking/<int:flight_id>',booking, name="booking"),
    path('booking_success/',booking_success,name='booking_success'),



   
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    