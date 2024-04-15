
//  Event listener to ensure DOM content has fully loaded
document.addEventListener("DOMContentLoaded", function () {
  const registerForm = document.getElementById("registerForm");

  /*
  * Ability to access the registerForm element and prevent default submission
  * An event listener that is triggered when the forms register button is clicked.
  * Use built in FormData constructor to build a set of key value pairs.
  * Then POST form data to server, then parse reponse as json 
  * Access the registration-messages data attribute for message to be displayed.
  * Then display either success or error and include bootstrap alert classes.
  * Reset form if registration is successful. 
  * Catch any errors
  */
  registerForm.addEventListener("submit", function (event) {
    event.preventDefault();

    const formData = new FormData(registerForm);

    fetch(registerForm.action, {
      method: "POST",
      body: formData
    })
      .then(response => response.json())
      .then(data => {

        const registrationMessage = document.querySelector("[data-registration-message]");

        if (data.success) {
          registrationMessage.innerHTML = `<div class="alert alert-success">${data.message}</div>`;
          registerForm.reset();
        } else {
          registrationMessage.innerHTML = `<div class="alert alert-danger">${data.message}</div>`;
        }
      })
      .catch(error => {
        console.error("An error has accured =", error);
      });
  });
});
