from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.conf import settings
from django.utils import timezone
from django.core.exceptions import ValidationError


# Create your models here. These models will be translated to tables in DB


# Model for enquiry form
class MakeEnquiry(models.Model):
    name = models.CharField(max_length=75)
    email = models.EmailField()
    heading = models.CharField(max_length=250)
    message_body = models.TextField()
    auto_acknowledge = models.BooleanField(default=False)
    date_submitted = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_submitted']
        indexes = [models.Index(fields=['-date_submitted']), ]

    def __str__(self):
        return f"Comment {self.heading} by '\
                         {self.name} on {self.date_submitted}"


# Model for comments form
class MakeComment(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE,
                                related_name='site_comments')
    email = models.EmailField()
    comment_message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.comment_message} by {self.creator}"


def validate_adults(value):
    if value < 1:
        raise ValidationError("Number of adults cannot be less than 1")


def validate_children(value):
    if value < 0:
        raise ValidationError("Number of children cannot be less than 0")


def validate_date(date):
    if date < timezone.now().date():
        raise ValidationError("Arrival date cannot be in the past")


# Model for Bookings form
class Booking(models.Model):
    name = models.CharField(max_length=75)
    email = models.EmailField()
    date_arrive = models.DateField(blank=False, validators=[validate_date])
    date_leave = models.DateField(blank=False, validators=[validate_date])
    adults_num = models.IntegerField(blank=False, validators=[validate_adults])
    child_num = models.IntegerField(blank=False,
                                    validators=[validate_children])
    slug = models.SlugField(max_length=250, null=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_arrive']
        indexes = [models.Index(fields=['-date_arrive']), ]

    def __str__(self):
        return f"Booking by {self.name}, arriving {self.date_arrive}"

    def get_absolute_url(self):
        return reverse("get_booking_form", kwargs={"slug": self.slug})


# model for the site capacity
class SiteCapacity(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('confirm', 'Confirm'),
        ('cancel', 'Cancel'),
    ]

    booking_date = models.DateField()
    slots_used = models.IntegerField()
    order_status = models.CharField(choices=STATUS_CHOICES, default='draft',
                                    max_length=10)

    class Meta:
        ordering = ['booking_date', 'order_status']
        indexes = [models.Index(fields=['booking_date', 'order_status',
                   'slots_used']), ]

    def __str__(self):
        return f"Date of booking {self.booking_date}, '\
                                  slots used {self.slots_used},'\
                                  status is {self.order_status}"
