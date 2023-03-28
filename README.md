![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# West Clare Motorhome Park
The last number of years, possibly aided by the COVID pandemic and associated travel constraints, have seen an explosion in Motorhome ownership in Ireland. There have been three fundamental responses to this growth, the first is a rise in the number of motorhome parks in Ireland or the expansion of traditional camp sites to cater for motorhomes. Secondly, slowly but surely some councils are seeing the benefit of creating Aires ( one night pull in points) in towns and villages to facilitate safe parking / waste disposal etc. Finally, some councils when faced with the sudden influx of motorhomes are reacting negatively and putting bars on parking facilities to restrict access to cars.

When a potential customer accesses a motorhome website, especially for a place they have not been before, they have a number of questions in mind that they need answered quickly and clearly. These questions include where exactly is the motorhome park, what facilities are available, what are the site rules , how far is the site from a town etc, how much does it cost per night?  This website answers all those questions clearly on the landing page. 

The site then moves to answering the question - what sites of interest are nearby? Where can I daytrip to or eat etc ? The Explore page shows a non exhaustive list of famous locations in West Clare and includes links to the home websites for those places.  

The contact page answers questions like , how can I contact the site owners, can I leave an enquiry? This page details the site telephone number and email address , it also incorporates an enquiry form which enables the visitor to place an enquiry.

There is a comments page, during development, this was de-prioritised and is included in the the future work section. Right now the user will see a placeholder image.

Finally there is a booking page. This page facilitates the user making a booking, deleting a booking and modifying a booking. Several attempts were made to incorporate capacity feedback i.e. the site is full on those dates please pick different dates however due to time constraints this will be added as future work. See capacity.py to direction this was going.

The final app can be found here https://motorhome-park-pp4.herokuapp.com/

![This is a picture of view from the park](/static/sunset_coast.PNG)


# Contents
1. [User Experience UX](#User-Experience-UX)
   * [Initial Discussion](#Initial-Discussion)
   * [User Stories](#User-Stories)
2. [Design](#design)
   * [Typography](#typography)
   * [Features](#features)
   * [Wireframes](#wireframes)
   * [Future Work](#futurework)
3. [Technologies Used](#technology-used)
4. [Data Models](#data-models)
5. [Deployment](#deployment)
6. [Testing](#testing)
7. [Credits](#credits)
<br />
<hr />
<br />

## User Experience UX

<br />

### Initial Discussion

As stated above, the number of motorhomes in private ownership and rented annually have increased dramatically. Waiting times for a new motorhome are between 9 months and 12 months. Many people seeking a motorhome park location are going online first and eciding based on their experience which site to stay at. 
The key motivations for a visitor to the site are:
* Desire to book a slot online for the motorhome park.
* Check that the site amenities / services meet the needs of the visitor.
* Check that areas of interest are indeed close to site.
* What are the site rules with respect to quiet times etc.



#### Key information for the site

* What are the views of the sea at the site.
* Can the visitor dispose of grey water and empty toilets on site.
* Are there electric hookups.
* A way for people to contact the site book club with questions.
* Schedule of fees for the year. 
* Can the visitor make a booking online. 
* Are there food options on-site or do you have to travel to food providers.

### User Stories

#### Visitor Goals

* As a visitor I want to quickly see where the site is located on a map.
* As a visitor I want to quickly see what transport options are availabale to me. 
* As a visitor I want to quickly see the schedule of charges for the current year. 
* As a visitor I want to quickly see what services are offered on site, including waste water disposal, showers etc. 
* As a visitor I want to quickly be assured around quiet times on the site and see behavioural guidelines. 
* As a visitor I want to quickly see what local attractions are close by so I can plan my day trips etc. 
* As a visitor I want to quickly see how to contact the site owners. 
* As a visitor I want to quickly be able to write an enquiry to the site owners and see that the enquiry has been acknowledged. 
* As a visitor I want to quickly be able to leave a review for others to read. 
* As a visitor I want to quickly be able to read reviews left by previous visitors. 
* As a visitor I want to be able to make a booking online and know the booking has been received. 
* As a visitor I want to be able to modify / change a booking online and know the booking has been updated. 
* As a visitor I want to be able to cancel a booking online aand know the booking has been cancelled. 

#### Site Owner Goals

* As a site owner I want the landing page to answer most of the potential visitors immediate questions.
* As a site owner I want access to an admin panel where I can action Enquiries, Bookings etc.
* As a site owner I want only the admin to have access to the admin panel.
* As a site owner I want to see a list of all enquiries in the admin panel. 
* As a site owner I want an automated email to be sent to the visitor to acknowledge receipt of an enquiry. 
* As a site owner I want to see a list of all non deleted bookings in the admin panel.
* As a site owner I want the visitor to be bale craete, Update and Cancel their own bookings only. 
* As a site owner I want to provide information to the viositor concerning attractions in the locality. 
* As a site owner I want the visitor to be able to leave comments and reviews and see reviews left by other visitors. 
* As a site owner I want the visitor to enjoy the website and comment on the site when talking to other motorhome owners. 
* As a site owner I want to receive an automated email telling me I have a new enquiry in the admin panel. 

<br />
<hr />
<br />

## 2. Design
### Typography
Google fonts was used to implement the Lato font across the website with Sans-Serif as backup.

### Features
#### Web Pages 
##### Home Page
The home page of the site is dominated by an image showing a view of the ocean from the motorhome site. It is precisely the kind of view that visitors would typically travel to see. The page also contains information to questions that potential visitors have when selecting a site such as where the site is, what amenities / services are onsite, what is the site code of conduct and what are the charges applied for the year in question. 
The colours used are mainly bootstrap standards (e.g text-primary, yexy-info etc) and are intended to make the page bright and interesting for a viewer. 
The page provides navigation links in the nav bar at the top of the page designed to enable the visitor to easily navigate to and fro on the site. The footer contains some general information about the site owners and includes social media links. The header and footer are common to all the site pages and are implemented by meams of a base.html which is extended across all the site pages.

![This is a picture of the site home page](/static/Site-page1.PNG)

<br />

#### Explore Page
The explore page details three of the main attractions near the site. This can be expanded in the future and is designed in bootstrap to show 3 images in a row and then collapse to one for smaller screeen sizes. 

![This is a picture of Explore Locally page](/static/explore-locally.PNG)

<br />

#### Enquiry Page
The Enquiry page shows a potential visitor the site telephone number and email address. The webpage also has a form that is built off a dataModel, to a form and then rendered to the template through a view. Once an Enquiry has been sent, the enquiry is logged to the admin panel for the site owner to review and respond, a message (jumbotron) is displayed to the screen to inform the visitor that their enquiry has been logged and will be responded to.

![This is a picture of the enquiry page](/static/web-enquiry.PNG)

#### Comment Page
The purpose of the comment page is to facilitate the creation of comments or site reviews. These site reviews would then available for other visitors to see and also of course for the site owners to review as feedback. This was deprioritised due to work load and will be completed in a future release.
<br />

#### Booking Page
The purpose of this page is to facilitate the visitor to make a booking through the webpage. The visitor may also modify an existing booking made by a user with their email address or delete / cancel a booking if required.
To make a booking the visitor is first asked to sign in or log in,
![This is a picture of the sign in needed page](/static/register.PNG)
<br />

The user is then brought to the sign in / sign up page
![This is a picture of the sign in needed page](/static/sign-up.PNG)
<br />

Once successfully logged in the user is presented with the booking form
![This is a picture of the booking form](/static/booking-form.PNG)
<br />

When a booking has been successful the user gets a message thanking them for their booking,the booking is available for the admin also on the admin panel
![This is a picture of the booking complete message](/static/booking-made.PNG)
<br />

When user clicks on link to modify a booking , all bookings with users email address are read from the database and presented in a list. The user can then either delete the booking or modify it.
<br />

![This is a picture of the list of bookings for a user](/static/modify-delete.PNG)
<br />

If the user deletes a booking then the following message is displayed:
<br />

![This is a picture of the booking deleted message](/static/booking-deleted.PNG)
<br />

When a booking has been modified, the user is returned to the delete / modify page and can confirm the changes by referencing the relevant booking.
<br />
<br />

### WireFrames
To see the wireframes for this app please ctrl+click here [wireframe.md](/wireframe)
<br />
<br />

### Future Work
<br />

* Reviews / comments functionality. It was intended to include this functionality in the initial release however due to time constraints this functionality will be included in a new release. The HTML form has been prepared, there is a placeholder graphic on the form currently. Also, the data model has been defined in models.py. The intent of the functionality is to provide a means to leave reviews / testimonials on the site for future visitors to review.
<br />

* Email functionality. It was intended that the system would be able to send automated email messages on submission of an enquiry and on submission of a booking. It was also intended to send emails to the site owner informing them that these events had occurred also. After multiple attempts and following online / online tutorials this functionality consistently failed. A future attempt will be made through DJango using JSmail as GMAIL and others using higher levels of authentication seem to have complicated this. Setting up a specific password for the app was not successful either. More to come...
<br />

* Site Capacity calculations. It was intended that when a user made a booking the system would check that there is space for each of the nights of the booking. Progress was made in that the arrive date and leave date were acquired from the request.POST object for the booking. These were then passed as parameters to a function which took the parameters, converted them to date objects and calculate a delta between the dates to establish the length of stay. Further more, code was written to identify each day in the range between arrive date and departure date. A for loop was then written to get the database entry from SiteCapacity that matches the date in question. Here a query matching error consistently occurred. I think the problem is that date format of the query did not match the date format in the table and several attempts to change the formats were not successful. Some of the code for this function can be viewed in capacity.py. More to come.....
<br />
<hr />
<br />

## 3. Technologies Used
The following technologies were used in this app:
* HTML / CSS and a small amount of javascript were used to design and style the webpages.
* Python3.8.11 was used for the Python coding.
* Django 3.2.18. provides the app framework.
* Bootstrap 5.3.0
* Google fonts was used to import the Lato font.
* Font Awesome provides icons throughout the site, especially Home page and Explore page.
* Git - used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* GitHub - used to store the projects code after being pushed from Git.
* Cloudinary - used to host / store images used in the app. 
* Heroku - used to host the final released web site.
* Postgres used as database.
<br />
<hr />
<br />



## 4. Data Models
There are 4 data models used in the app and these data models are defined in the models.py file. The models are:
* MakeEnquiry model - this model defines the fields for Enquiry table in the Database.
* MakeComment model - this model defines the fields for the Comment table in the Database.
* Booking model - this model defines the fields for the booking database.
* SiteCapacity model - this model defines the fields for the site capacity table. It holds a date and number of slots used for that date.

There are 3 form classes defined and these are built from the data models defined in models.py.
* EnquiryForm uses the MakeEnquiry model and defines fields to be visible on the form. This form is how a user posts an Enquiry.
* CommentForm use the MakeComment model and defines fields to be visible on the form. Not released in initial release. See future work.
* BookingForm uses the Booking model and defines fields to be visible on the form. The date_arrive field has validation to ensure that the arrival date is not sooner than booking date ( today ). Date_arrive and date_leave also have placeholders to show the user that the US date format is in use.

There 7 views to render templates with forms and control redirects etc.
* get_enquiry_form view renders the Enquiry form to the Enquire.html template. This view also sends a variable called 'sent' back to the template, 
'sent' is used to control whether or not a success Jumbtotron is renedered to the template or not.
* get_booking_form view renders the booking form to the booking.html template. The view also prepopulates the form email field to be the authenticated user name, a success message is output when a booking is successfully made.
* get_index_form, get_explore_form, get_comment_form are used to render the static pages Index.html, explore.html while the comment.html will be completed as part of future work. 
* get_cancel_booking_form view renders the cancel_booking.html template and displays booking filtered by booking_id to ensure a user only sees their own bookings.
* get_modify_booking_form view renders the modify_booking.html template. It allows a user to change their own bookings only. 

CRUD operations.
CRUD operation requirement satisfied as follows;
* Create - within the app the user has the capability to create both enquiries and bookings and persist them to the database.
* READ - as part of the booking functionality, bookings filtered by booking_ID are read from the database and presented to the user.
* UPDATE - as part of the booking functionality, a user can update/modify their own bookings.
* DELETE - as part of the booking functionality, a user has the capability to delete their own bookings.

Agile planning
GITHUB projects and issues were used to create user stories and move these stories through the process at various stages. 
Please see agile.md ctrl-click here [agile.md](/agile)



## 5. Deployment





## 6. Testing
## 7. Credits
* https://ordinarycoders.com/django-bootstrap
* https://bootstrapious.com/p/bootstrap-navbar#navbar-header
* https://www.sitepoint.com/django-send-email/
* https://learndjango.com/tutorials/django-login-and-logout-tutorial
* https://www.geeksforgeeks.org/datefield-django-forms/
* https://nsikakimoh.com/blog/how-to-use-messages-in-django
* https://stackoverflow.com/questions/35465557/how-to-apply-color-on-text-in-markdown
* https://www.w3schools.com/bootstrap4/bootstrap_colors.asp
* https://stackoverflow.com/questions/65337432/markdown-links-to-external-markdown-documents
* https://stackoverflow.com/questions/28261287/how-to-change-btn-color-in-bootstrap
* https://realpython.com/search?kind=article&kind=course&order=newest
* https://docs.djangoproject.com/en/4.1/
* Django 4 by example, Antonio Mele.
* https://getbootstrap.com/docs/5.0/utilities/background/


