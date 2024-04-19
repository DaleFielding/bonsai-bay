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
  * Error = Duplicate id ‘email’ one in base template and one in account template, fixed by renaming the if in account template as well as the relevant data-bs-target
  * Warning = Min and max attributes not allowed in textarea (x2), I have removed these
  * Warning  = Accidentally included `]`  as an attribute within a textarea, fixed by removing this.
  * After these changes, no errors or warnings displayed

* Item page: 
  * No errors or warnings to show.
