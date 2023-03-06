from .models import MakeComment, MakeEnquiry, Booking
from django import forms


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = MakeEnquiry
        fields = ['name', 'email', 'heading', 'slug', 'message_body',
                  'auto_acknowledge', 'date_submitted']


class CommentForm(forms.ModelForm):
    class Meta:
        model = MakeComment
        fields = ['creator', 'email', 'comment_message', 'created_on', 
                  'approved']


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'date_arrive', 'date_leave', 'adults_num',
                  'child_num', 'slug', 'confirmed']





