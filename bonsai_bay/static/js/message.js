/** messageSent function:
* Prevent defaults submission.
* Accesses the data attribute data-message-sent.
* Changes the innerHtml when send button is clicked
* Message times out after 2 seconds, changing innerHTML
**/
function messageSent(event) {
  event.preventDefault();
  document.querySelector("[data-message-sent]").innerHTML
    = "Your message has been sent";
  setTimeout(function () {
    document.querySelector("[data-message-sent]").innerHTML
      = "&nbsp;";
  }, 2000);
}