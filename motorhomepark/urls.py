from motorhomepark.views import (get_enquiry_form, get_booking_form,
                                 get_explore_form, get_index_form,
                                 get_comment_form, get_confirm_form)
from django.urls import path, include


urlpatterns = [
     path('', get_index_form, name='get_index_form'),
     path('enquiry/', get_enquiry_form, name='get_enquiry_form'),
     path('explore/', get_explore_form, name='get_explore_form'),
     path('booking/', get_booking_form, name='get_booking_form'),
     path('comment/', get_comment_form, name='get_comment_form'),
     path('confirm/', get_confirm_form, name='get_confirm_form'),
     path("accounts/", include("allauth.urls")),
]