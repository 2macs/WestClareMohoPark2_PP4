# Pseudocode for this application

## Enquiry page
On this page the user will be presented with an enquiry form. The intent of this form is that user will simply craft an enquiry and submit it. One the enquiry has been submitted, the user will be presented with a message saying the enquiry has been received and user will receive a response soon. The Enquiry form will be based on a data model called MakeEnquiry, the view for this model is called get_enquiry_form and the form is then rendered to enquire.html file. There should be validation on all fields except the message / body field which may be blank. The form should be well laid out and look good / correct across different screen sizes. Once an enquiry has been submitted by the user, the site owner should be able to see enquiries on the admin page and acknowledge the enquiry once it has been answered. It is not required that the user can Update or Delete an enquiry once submitted. It is not required that a user can go in and see a list of their enquiries. The intent is a simple straightforward communication to the site owner and the response from the site owner can be by telephone or email and not controlled through this application.

## Booking Form
To make a booking the user must first login to the application, 

The intent of the booking form is allow a user to :
* Make a booking for the website across a number of days.
* The application will then check to see if there is availability for those dates.    
* If there is no availability then the user will be advised and asked to return to the booking page to select different dates.
* Once a booking is "valid" the user will get feedback concerning the name on the booking, dates being booked, estimate of costs.
* User will be asked to confirm booking. ( CREATE booking ), this will persist the booking to database. This will increment bookings for that date in DBase also.
* The user will be login later and see / view all bookings made by the user ( READ bookings).
* The user will be able to edit / change a booking if required (UPDATE booking), note if updating dates then checks for availability 
    will be re-executed with messages etc. 
* The user will be able to cancel a booking if circumastances change ( DELETE booking ), if a booking is deleted then message confirming this to be output to user, message to site owner also. This will decrement slot usage for that date in DBase.
* In admin panel, site owner should be able to see Draft bookings, confirmed bookings and deleted bookings and filter accordingly.
* In admin panel, site owner should be able to see dates and slot usage.

## Site capacity
The capacity of the site will be modelled by means of a data model containing a date field and number of slots actually booked for that date. A constant for site capacity will be added to settings.py. When a booking is being made the application will check each date and check that current usage + 1 is less that the site capacity as defined in settings.py. If it is then the booking will be valid and the user will get option to confirm the booking. When a booking is cancelled / deleted , then for each date of the booking the slots actually booked must be decremented by 1. 


