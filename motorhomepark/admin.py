from django.contrib import admin

# Register your models here.
from .models import MakeEnquiry, Booking, MakeComment, SiteCapacity


@admin.register(MakeEnquiry)
class EnquiryManage(admin.ModelAdmin):
    display_all = ['heading', 'slug', 'name', 'date_submitted']
    list_filter = ['date_submitted', 'name', 'heading']
    search_fields = ['heading', 'message_body']
    date_hierarchy = 'date_submitted'


@admin.register(Booking)
class BookingManage(admin.ModelAdmin):
    display_all = ['name', 'slug', 'date_arrive', 'email']
    list_filter = ['date_arrive', 'name', 'email']
    search_fields = ['name', 'date_arrive', 'email']
    prepopulated_fields = {'slug': ('name', )}
    date_hierarchy = 'date_arrive'


@admin.register(MakeComment)
class CommentManage(admin.ModelAdmin):
    display_all = ['creator', 'slug', 'created_on', 'approved']
    list_filter = ['creator', 'created_on', 'approved']
    search_fields = ['creator', 'created on', 'email']
    date_hierarchy = 'created_on'

@admin.register(SiteCapacity)
class SiteManage(admin.ModelAdmin):
    display_all = ['booking_date', 'slots_used', 'order_status']
    list_filter = ['booking_date', 'slots_used', 'order_status']
    search_fields = ['booking_date', 'slots_used', 'order_status']
    date_hierarchy = 'booking_date'
