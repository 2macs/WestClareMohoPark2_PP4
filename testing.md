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
   * [Typography](#typography)
   * [Features](#features)
   * [Wireframes](#wireframes)
   * [Future Work](#futurework)

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
