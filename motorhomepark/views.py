from django.shortcuts import render, redirect, get_object_or_404
from .forms import EnquiryForm, BookingForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from mohoparkR2 import settings
from motorhomepark.models import Booking


# Create your views here.
# Templates are Index, booking,enquire,explore

def get_enquiry_form(request):
    sent = 0
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            sent = 1            
    else:
        form = EnquiryForm()
    return render(request, 'enquire.html/', {'form': form, 'sent': sent})


# Create a booking
def get_booking_form(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = BookingForm()
    return render(request, 'booking.html/', {'form': form})


def get_index_form(request):
    return render(request, 'index.html/')


def get_explore_form(request):
    return render(request, 'explore.html')


def get_comment_form(request):
    return render(request, 'comment.html')


def get_confirm_form(request):
    return render(request, 'confirm.html')


def get_cancel_booking_form(request):
    user_name = request.user.username
     # Retrieve all Booking records of the logged-in user
    bookings = Booking.objects.filter(email=user_name)
    print(user_name)
    
    if request.method == 'POST':
        booking_id = request.POST.get('id')
        booking = Booking.objects.get(id=id)
        booking.delete()
        return redirect('get_booking_form')
    # Render the template with the list of Booking records
    return render(request, 'cancel_booking.html', {'bookings': bookings})
