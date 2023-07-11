## Contents
<br />
<hr />
<br />

1. [AUTOMATED TESTING](#AUTOMATED-TESTING)
  * [W3C Validator](#W3C-Validator)
  * [JavaScript Validator](#JavaScript-Validator)
  * [Python Validator](#Python-Validator)
  * [Lighthouse](#Lighthouse)
2. [Detailed Testing](#detailed-testing)


### Automated Testing
<br />

#### W3C Validator
The following HTML pages were tested:
* Index.html - No errors or warnings to show.
* Explore.html - No errors or warnings to show.
* Enquire.html - No errors or warnings to show.
* Comment.html - No errors or warnings to show.
* Booking.html - No errors or warnings to show.
* Modify_booking.html - There was an error on initial submission, no error present now
CSS validator - No errors.

#### Javascript validator
N/A only one js function defined to generate an alert. 

#### Python Validator
<br />

* Views.py <br />
![Linter result for views.py](/static/views_linter.PNG)
<br />
<br />

* urls.py <br />
![Linter result for urls.py](/static/urls-linter.PNG)
<br />
<br />

* models.py <br />
![Linter result for models.py](/static/models-linter.PNG)
<br />
<br />

* forms.py <br />
![Linter result for forms.py](/static/forms-linter.PNG)
<br />
<br />

* Date_check.py and capacity.py not tested as not used. Potentially used in the future.
<br />
<br />

* apps.py <br />
![Linter result for apps.py](/static/apps-linter.PNG)
<br />
<br />

* admin.py <br />
![Linter result for admin.py](/static/admin-linter.PNG)
<br />
<br />





#### Lighthouse
<br />
Lighthouse recomended using smaller image sizes. For this release will stay with existing images and look to compress images for future releases. <br />

Index Form <br />
![Lighthouse result for site](/static/lh-index.PNG)
<br />
Explore Form <br />

![Lighthouse result for explore](/extra_pics/lh-explore.PNG)
<br />
Enquiry Form <br />

![Lighthouse result for Enquiry](/extra_pics/lh-enquiry.PNG)
<br />
Comment Form <br />

![Lighthouse result for Comment](/extra_pics/lh-comment.PNG)
<br />
Booking Form <br />

![Lighthouse result for Booking](/extra_pics/lh-booking.PNG)

<br />
<hr />
<br />


### Detailed Testing

| Test                  | Expected       | Actual        |Result            |
|-----------------------|----------------|---------------|------------------|     
|Navigation             |                |               |                  |
|Test nav bar links all pages|Pages open as expected     |Pages change as expected|Pass   |
|Header correct all forms| Header is consistent| Header is as expected|Pass|
|Footer is consistent all forms|Same footer all forms|Footer is consistent|Pass|
|Home Page              |                |               |                 |
|Sea view on site and clear|View on home page|View present|Pass |
|Overview, Directions, Transport beside image|Clear messaging|Text is present, bright colour|Pass|
|Amenities display services|Text stands out, easy to read|Text accurate and easy to read|Pass|
|Pricing is clear and accurate|Pricing easy to find|Pricing accurate, page center|Pass|
|Code of conduct is clear and accurate|Easy to read, easy to find|Text accurate, easy to find|Pass|
|Image showing site location|Image showing site location|Image is present, pin represents site|Pass|
|Explore Locally|   |   |   |
|   |  |    |
|Cliffs of Moher image and text present|Image is clear, text is accurate|Image and text present|Pass|
|Cliffs of moher link available|Open link in new tab|Opened in new tab|Pass|
|Surfing in Lahinch image and text available|Image is clear, text is accurate|Image and text present|Pass|
|Surfing in Lahinch link available|Open link in new tab|Opened in new tab|Pass|
|Burren adventure center image and text available|Image is clear, text is accurate|Image and text present|Pass|
|Burren adventure center link present|Open link in new tab|Opened in new tab|Pass|
|Enquiry Form |  |   |   |
|Enquiry form rendered to screen|Name, email,heading , message body|Form rendered correctly|Pass|
|Create enquiry and save|Success message|Success message appears|Pass|
|Click Ok on message|Return to home page|Returned to home page|Pass|
|Login as admin|Enquiry visible in admin panel|Enquiry logged to Make Enquiry panel|Pass|
|Logout of admin|Return to home page|Returned to home page|Pass|
|Leave a comment|   |   |  |
|Page under construction|Image showing page under construction|Image present|Pass|
|Manage Bookings|  |   |   |
|User not booked in|User directed to sign in page|Sign in page appears|Pass|
|User not logged in|Click Ok to return to home page|Returned to home page|Pass|
|User log in not logged in before|Use francis Black,direct to sign up page|The username and or password not correct|Pass|
|Create user francis.black@hotmail.com|use pword 11223344|Error password is fully numeric|Pass|
|Create user francis.black@hotmail.com|use pword!11223344!|see successfully signed in message|Pass|
|Create a clean booking , all fields|Booking created|see booking completed message|Pass|
|Select cancel an existing booking|Should see a list of bookings by Francis Black|Booking just made is avaialable|Pass|
|Create a booking, no fields completed|Error asking for name to be filled in|Request to fill in name field|Pass|
|Create a booking, all fields except arrival date|Request to fill in arrival date|Request to fill out arrival date|Pass|
|Create a booking for arrival date before today|Error saying cant arrive before current date|Error Arrival date cannot be in the past|Pass|
|Create a booking for departure date before today|Error saying cant arrive before current date|Error Arrival date cannot be in the past|Pass|
|Create a booking for adults less than 1|Error saying Number of adults cannot be less than 1|Error Number of adults cannot be less than 1|Pass|
|Create a booking for children less than 0|Error saying Number of children cannot be less than 0|Error Number of children cannot be less than 0|Pass|
|Click on To cancel an existing booking|Bookings made by Francis Black|2 bookings made by Francis Black|Pass|
|Delete first booking|Get message confirming deletion, redirect to booking page|Message Booking deleted, please re-book if required|Pass|
|Click on to cancel an existing booking|Deleted booking no longer on list|Deleted booking gone|Pass|
|Stay in current form, click update booking button on remaining booking|see this specific booking on screen|Booking correct|Pass|
|Change the value of the adults field to some other number|Number should be changed to 2|Number chnaged to 2 adults|Pass|
|Logout Francis Black|SHould get Are you Sure message|Message received|Pass|
|Login as admin|Successful login|Message saying login successful|Pass|
|Navigate to admin panel|See Enquiry / booking tables avaialble| Avaialable as expected|Pass|
|Look for enquiry just created and booking just created|Present in respective lists|Present as expected|Pass|


#### Bugs
<br />

* The Navbar heading 'West Clare Motorhome Park (extended through the header) is not fully responsive, on very small screens parts of the heading disappears from view. I have tried to define a media query to change the font size once a certain screen size is met but this hasn't worked. Also have tried inline bootstrap to change the size but to date this hasn't worked either. Am consulting with a professional on this and will fix for next release.

* When a user logs in, if another user has just logged out - Django generates a 'you have logged out' message' on the same screen as 'You have successfully logged in' . This seems to be a question asked on various forums and playing with the redirect on logout constant seems to be the fix. At this point am highlighting this and will fix / remove for next release.

* On the booking form, there is validation preventing a user from inputting an arrival date earlier than the current date. At the moment there is no validation preventing a user from defining a departure date earlier than the arrival date. I spent significant time trying to figure this out and also contacted tutor support who could not help immediately. I expect this will be fixed with next release. 
















