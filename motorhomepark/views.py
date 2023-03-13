from django.shortcuts import render, redirect
from .forms import EnquiryForm
from mohoparkR2 import settings


# Create your views here.
# Templates are Index, booking,enquire,explore

def get_enquiry_form(request):
    
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_confirm_form')
    else:
        form = EnquiryForm()
    return render(request, 'enquire.html/', {'form': form})


def get_booking_form(request):
    return render(request, 'booking.html')


def get_index_form(request):
    return render(request, 'index.html/')


def get_explore_form(request):
    return render(request, 'explore.html')


def get_comment_form(request):
    return render(request, 'comment.html')


def get_confirm_form(request):
    return render(request, 'confirm.html')



