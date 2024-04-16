// Event listener to ensure DOM content has fully loaded
document.addEventListener("DOMContentLoaded", function () {
  const loginForm = document.getElementById("loginForm");

  /*
  * Access the loginForm element and prevent default submission
  * An event listener that is triggered when the form's login button is clicked.
  * Use built in FormData constructor to build a set of key value pairs.
  * Then POST form data to server, then parse response as json 
  * Access the login-message data attribute for message to be displayed.
  * Then display either success or error and include bootstrap alert classes.
  * If login is successful, redirect to account page.
  * Catch any errors
  */
  loginForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(loginForm);

    fetch(loginForm.action, {
      method: "POST",
      body: formData
    })
      .then(response => response.json())
      .then(data => {

        const loginMessage = document.querySelector("[data-login-message]");

        if (data.success) {
          loginMessage.innerHTML = `<div class="alert alert-success">${data.message}</div>`;
          window.location.href = "/account";  // Redirect to account page
        } else {
          loginMessage.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
        }
      })
      .catch(error => {
        console.error("An error has occurred =", error);
      });
  });
});