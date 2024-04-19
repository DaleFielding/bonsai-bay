# Testing

I have considered the testing approaches for this project; automated versus manual.

I believe automated testing works well when tests would take a very long time to do manually, or if tests need to be repeated over and over again. 
I believe that manual testing can be better when you only need to run a test a couple of times.

For this project, I have used manual testing throughout development and post development so that I can take a hands-on approach and ensure everything works smoothly.

## Validation 
### WSC - Markup Validation Service
* Homepage (including base.html and index.html):
  * Error = button type attribute not allowed on div. Fixed this my changing the attribute to role=”button”.
  * Warning = aria-label not valid for twitter `<i>` element, corrected this by moving the aria-labels to the containing `<a>` element instead.
  * After these changes, no errors or warnings displayed.

* Browse bonsai:
No errors or warnings displayed.

* 404 page:
  * No errors or warnings displayed.

* Account page:
  * Error = HTTP resource not retrievable (401). This is due to the authentication required before the account page can be accessed. Fixed this by adding logic to the account route that handled the absence of a user being logged in. Also temporarily commented out login_required so that the template could run through the validator.
  * Error = Duplicate id ‘email’ one in base template and one in account template, fixed by renaming the if in account template as well as the relevant data-bs-target.
  * Warning = Min and max attributes not allowed in textarea (x2), I have removed these.
  * Warning  = Accidentally included `]`  as an attribute within a textarea, fixed by removing this.
  * After these changes, no errors or warnings displayed.

* Item page: 
  * No errors or warnings to show.

### WSC - CSS Validation Service
I have entered my external css file into the validator:
* No errors found.
* Warnings appear in relation to using variables for the colours/fonts. I have left these in as css variables were taught in one of the codeinstitute lessons.

### Wave - Web Accessible Evaluation Tool
* Error = Search-bar input didn't have a corresponding label, I have added this now but made sure it is visually hidden.
* Error = 2x buttons that were empty, I have changed these elements to divs. These are currently just for display purposes, as functionality will be in future implimentations.
* Error = 1x button said to be empty, although has an icon as the value. I have fixed this by adding an aria-label for screen readers.
* Warning = Missing first level headings, changed `<h2>` to`< h1>` and `<h3>` to `<h2>`.
* Warning = Skipped level heading, referring to the `<h6>` tags for the listing titles, fixed these by changing to `<h4>` tags.
* Warning = redundant link as there is more than one link for home on the navbar, this was on the logo and the site name which are next to each other. Fixed by combining into one anchor tag.
* Warning = Redundant links for ‘Browse Bonsai’ as there is a link for this in the navbar and a link below the intro message on the main page. I have left this in as believe it is a key part in the design. This only happens on the homepage.

