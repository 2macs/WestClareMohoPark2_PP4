from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.conf import settings

# Create your models here. These models will be translated to tables in DB


# Model for enquiry form
class MakeEnquiry(models.Model):
    name = models.CharField(max_length=75)
    email = models.EmailField()
    heading = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    message_body = models.TextField()
    auto_acknowledge = models.BooleanField(default=False)
    date_submitted = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_submitted']
        indexes = [models.Index(fields=['-date_submitted']),]

    def __str__(self):
        return f"Comment {self.heading} by {self.name} on {self.date_submitted}"


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


# Model for Bookings form
class Booking(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, related_name="booking_owner")
    email = models.EmailField()
    date_arrive = models.DateField()
    date_leave = models.DateField()
    adults_num = models.IntegerField()
    child_num = models.IntegerField()
    slug = models.SlugField(max_length=250, unique=True)
    confirmed = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_arrive']
        indexes = [models.Index(fields=['-date_arrive']),]

    def __str__(self):
        return f"Booking by {self.name}, arriving {self.date_arrive}"


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
                   'slots_used']),]

    def __str__(self):
        return f"Date of booking {self.booking_date}, booked by {self.person}, status is {self.order_status}"

