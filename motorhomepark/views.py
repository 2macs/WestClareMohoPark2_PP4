from django.shortcuts import render
from .forms import EnquiryForm
from mohoparkR2 import settings
from django.core.mail import send_mail, EmailMessage



# Create your views here.
# Templates are Index, booking,enquire,explore

def get_enquiry_form(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            # put email logic here
            email = request.POST['email']
            user_name = request.POST['name']
            email_sender = settings.EMAIL_HOST_USER
            subject = f'Your Enquiry to West Clare Motorhome Park'
            email_response = f'Hi {email}, thank you for your enquiry, we will respond as soon as possible!'
            message_to_owner = f'Hi, you have received an enquiry from {user_name}, please check your admin page'
            send_list = [email, ]
            to_owner = [email_source, ]
            email = EmailMessage('subject', 'email_response', to=['email'])
            email.send()
            # send_mail(subject, email_response, email_sender, send_list)
            return HttpResponseRedirect('/')
            # send_mail(subject, message_to_owner, email_sender, to_owner)
            return redirect('index/')
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



