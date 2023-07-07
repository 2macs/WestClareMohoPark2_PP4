from .models import MakeComment, MakeEnquiry, Booking
from django import forms
from django.utils import timezone
from django.core.exceptions import ValidationError


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = MakeEnquiry
        fields = ['name', 'email', 'heading', 'message_body']


class CommentForm(forms.ModelForm):
    class Meta:
        model = MakeComment
        fields = ['creator', 'email', 'comment_message', 'approved']


def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Arrival date cannot be in the past")


class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ['name', 'email', 'date_arrive', 'date_leave', 'adults_num',
                  'child_num']
        widgets = {
            'date_arrive': DateInput(),
            'date_leave': DateInput(),
        }
