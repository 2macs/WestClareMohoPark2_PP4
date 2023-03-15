from django.shortcuts import render, redirect
from .forms import EnquiryForm, BookingForm
from mohoparkR2 import settings


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


def get_booking_form(request):
    form = BookingForm()
    return render(request, 'booking.html', {'form': form})


def get_index_form(request):
    return render(request, 'index.html/')


def get_explore_form(request):
    return render(request, 'explore.html')


def get_comment_form(request):
    return render(request, 'comment.html')


def get_confirm_form(request):
    return render(request, 'confirm.html')



