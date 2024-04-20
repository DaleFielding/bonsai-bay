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

### JSLint
All of my JavaScript for this project has been put through JSLint.
A common warning appears in reference to ‘document’ not being declared throughout JavaScript code. <br>These warnings are unnecessary and I have removed them when using the linter by adding
``` /*jslint browser:true */``` to the top of the page.<br>
Details of the JSLint results for each page can be seen below:

#### Location.js:
* Warning = Regarding undeclared 'fetch'. Have resolved by placing /*global fetch */ to make jslint aware that this is intentionally used.
* Warning = To use double quotes instead of single quotes within functions. Fixed by amending these.
* Warning = Expected use of ‘await’ as ‘async’ was used. Looking at the function I noticed that there was no need to have async on the outer function as there is a async - await logic within an inner function. Removed async from the outer function.
* Warning = Line of code of 80 characters long. I have resolved this by splitting this over 2 lines.
* Warning = JSlint didn’t like this line ‘if ("geolocation" in navigator)’, suggested that I Compare with undefined, or use the hasOwnProperty method instead. I have amended the function to compare with undefined; function still works as desired after the amendment.
* Warning = About a line of code that isn’t in my files at all (eval("console.log(\"hello world\");");. I have used the magnifying glass search to try and locate this, have also searched to see if it is contained within a module; it isn’t. I can only assume this must be an error with JSlint.
* Functionality still works as expected after these changes

#### Login.js:
* Warning  = Unexpected trailing space. Fixed by removing this
* Warning = JSlint didn’t like a couple of arrow functions having complexity. I have fixed these by changing to a traditional function
* Warning = A few lines longer than 80 characters. Fixed these by splitting into two lines
* Warning = Undeclared Jquery symbol. Added JQuery symbol the same comment as global fetch in order to pass JSlint
* Warning = Suggested double quotes be used instead of single quotes inside functions. Fixed by amending these.
* Warning = Expected property 'body' to be ordered before property 'method'. Fixed by swapping them around
* Warning = Post method is unexpected. The logic to handle this method is server side so I have not made any amendments to this.
* Functionality still works as expected after these changes

#### Register.js:
* Warning = Expected property 'body' to be ordered before property 'method'. Fixed by swapping them around
* Warning = Post method is unexpected. The logic to handle this method is server side so I have not made any amendments to this.
* Warning = A few lines longer than 80 characters. Fixed these by either splitting into two lines, or reducing comment size.
* Warning = JSlint didn’t like a couple of arrow functions having complexity. I have fixed these by changing to a traditional function 
* Warning = Some lines with trailing spaces. Fixed by removing these
* Warning = Suggested double quotes be used instead of single quotes inside functions. Fixed by amending these.
* Functionality still works as expected after these changes

#### Search.js:
* Warning = A couple of line longer than 80 characters. Fixed these by either splitting into two or more lines.
* Warning = Some lines with trailing spaces. Fixed by removing these
* Warning = Suggested double quotes be used instead of single quotes inside functions. Fixed by amending these.
* Warning = Expected closing brace and instead saw backtick. There are no problems in the terminal and function works are expected. I can only assume JSLint seems to be having issues with backticks as were not previously supported.
* Functionality still works as expected after these changes.

### CI Python Lynter:
#### __init__.py:
* A couple of lines longer than 80 characters. Fixed by reducing the amount of words used.
* No new line space at the end of the file. Fixed by adding a newline at the end.
* Module level import not at top of file; referring to `from bonsai_bay import routes`. This position is required for the app to function correctly, so I am leaving this where it is.

#### Models.py: 
* No errors found or amendments needed.

#### Routes.py:
* Quite a few of lines longer than 80 characters. Fixed by reducing the amount of words used or splitting over two/three lines, sometimes using `\` to show it is a continuation of the same line
* Blank line contained a whitespace. Fixed by removing this.

#### App.py:
* No errors found or amendments needed.

#### Env.py:
* One line longer than 80 characters. Fixed this by splitting across 3 lines.


