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
4. [Deployment](#deployment)
5. [Testing](#testing)
6. [Credits](#credits)
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
To see the wireframes for this app please click here [wireframe.md](/wireframe)
<br />
<br />







































## 3. Technologies Used
## 5. Testing
## 6. Credits

