from motorhomepark.views import (get_enquiry_form, get_booking_form,
                                 get_explore_form, get_index_form,
                                 get_confirm_form,
                                 get_cancel_booking_form,
                                 get_modify_booking_form)
from django.urls import path, include


urlpatterns = [
     path('', get_index_form, name='get_index_form'),
     path('enquiry/', get_enquiry_form, name='get_enquiry_form'),
     path('explore/', get_explore_form, name='get_explore_form'),
     path('booking/', get_booking_form, name='get_booking_form'),
     path('confirm/', get_confirm_form, name='get_confirm_form'),
     path('cancel_booking', get_cancel_booking_form,
          name='get_cancel_booking_form'),
     path('modify_booking/<int:booking_id>', get_modify_booking_form,
          name='get_modify_booking_form'),
     path("accounts/", include("allauth.urls")),
     ]
