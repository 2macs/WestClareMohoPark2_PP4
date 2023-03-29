from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import EnquiryForm, BookingForm
from django.contrib.auth.decorators import login_required
from django.views import generic
from mohoparkR2 import settings
from motorhomepark.models import Booking, SiteCapacity
from datetime import date, datetime, timedelta


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
    form = BookingForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request,
                             'Booking completed, see you soon!')
            return redirect('get_booking_form')
    else:
        initial = {'email': request.user.username}
        form = BookingForm(initial=initial)
    return render(request, 'booking.html/', {'form': form})


def get_index_form(request):
    return render(request, 'index.html/')


def get_explore_form(request):
    return render(request, 'explore.html')


def get_comment_form(request):
    return render(request, 'comment.html')


def get_confirm_form(request):
    return render(request, 'confirm.html')


# Delete a booking
def get_cancel_booking_form(request):
    user_name = request.user.username

    # Retrieve all Booking records of the logged-in user
    bookings = Booking.objects.filter(email=user_name)

    if request.method == 'POST':
        mybooking = request.POST.get('booking_id')
        booking = Booking.objects.get(id=mybooking)
        booking.delete()
        messages.warning(request,
                         'Booking deleted, please re-book if required')
        return redirect('get_booking_form')
    # Render the template with the list of Booking records
    return render(request, 'cancel_booking.html', {'bookings': bookings})


# Modify a booking
def get_modify_booking_form(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)

    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()

        return redirect('get_cancel_booking_form')
    else:
        form = BookingForm(instance=booking)
        context = {'form': form}

    return render(request, 'modify_booking.html',
                  context)
