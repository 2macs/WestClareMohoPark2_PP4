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
        # get the arrival date and the leave date from the request
        arrival_date = (request.POST.get('date_arrive'))        
        leave_date = request.POST.get('date_leave')
        
        print(f'Before passing to function, arrival date is {arrival_date}, leave date is {leave_date}')
        check_booking_dates(arrival_date, leave_date)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for your booking, we look forward to seeing you soon!')
            return redirect('/')
    else:
        initial = {'email':request.user.username}
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
        return redirect('get_modify_booking_form', booking_id=booking.id)        
    else:
        form = BookingForm(instance=booking)
        context = {'form': form}

    return render(request, 'modify_booking.html', 
                  context)


def check_booking_dates(start_date, end_date):
    print(f'The function was called.... with {start_date} and {end_date}')
    date_object = datetime.strptime(start_date, '%m/%d/%Y').date()
    date_object2 = datetime.strptime(end_date, '%m/%d/%Y').date()
    # confirm the dates are correct,
    print(f'After processing to date objects .... with {date_object} and {date_object2}')

    check_list = SiteCapacity.objects.all()
    for check in check_list:
        print('loop running')
        print(f'{check.booking_date} slots used {check.slots_used}')

    # loop through the dates
    # delta = date_object2 - date_object
    # for i in range(delta.days):
    #     myDay = date_object + timedelta(days=i) # this is correct number of days
    #     site_capacity = SiteCapacity.objects.get(booking_date=myDay)
    #     space_used = site_capacity.slots_used
    #     print(f'Date: {site_capacity}, space used :{space_used}')
    


    
