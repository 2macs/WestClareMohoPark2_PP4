"""mohoparkR2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from motorhomepark.views import (get_enquiry_form, get_booking_form,
                                 get_explore_form, get_index_form,
                                 get_comment_form)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', get_index_form, name='get_index_form'),
    path('enquiry/', get_enquiry_form, name='get_enquiry_form'),
    path('explore/', get_explore_form, name='get_explore_form'),
    path('booking/', get_booking_form, name='get_booking_form'),
    path('comment/', get_comment_form, name='get_comment_form'),
]
