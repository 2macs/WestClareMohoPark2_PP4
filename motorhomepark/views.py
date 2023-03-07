from django.shortcuts import render

# Create your views here.
# Templates are Index, booking,enquire,explore


def get_enquiry_form(request):
    return render(request, 'templates/enquire.html')


def get_booking_form(request):
    return render(request, 'templates/booking.html')


def get_index_form(request):
    return render(request, 'index.html/')


def get_explore_form(request):
    return render(request, 'templates/explore.html')


def get_comment_form(request):
    return render(request, 'templates/comment.html')
