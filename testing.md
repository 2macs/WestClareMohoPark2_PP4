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
* Modify_booking.html - One error on line 66, "anchor tag cannot be a child of button tag". Functionality works and some sites recommend this approach. Fix for next release.
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

![Lighthouse result for site](/static/lh-index.PNG)
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






