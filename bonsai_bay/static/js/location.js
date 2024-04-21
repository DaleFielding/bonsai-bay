/*global fetch, navigator, console*/

/**
* determineCity async function:
* Passes in latitude and longitude coordinates.
* Fetches the city name and returns.
* Returns null is city isn't found.
**/
async function determineCity(latitude, longitude) {
  const response = await fetch(`/get_city/${latitude}/${longitude}`);
  const city = await response.text();
  return city !== 'City not found' ? city : null;
}

/**
* Access 'data-get-location' element to add a click event
* Check if geolocation is supported
* If succesful it gets the users position and determines the city
* If city found, updates 'location' element value.
* If not, displays an alert that says No city found or location access denied.
* Also alerts user if geolocation not supported
* Displays any errors within the innerHTML, adding bootstap alert styling.
**/
document.querySelector("[data-get-location]")
  .addEventListener("click", function () {
    try {
      if (navigator.geolocation !== undefined) {
        navigator.geolocation.getCurrentPosition(async function (position) {
          const latitude = position.coords.latitude;
          const longitude = position.coords.longitude;
          const city = await determineCity(latitude, longitude);
          const cityFoundMsg = document.querySelector("[data-city-found]");
          if (city) {
            document.getElementById("location").value = city;
            cityFoundMsg.innerHTML =
              `<div class="alert alert-success">Location found</div>`;
          } else {
            cityFoundMsg.innerHTML =
              `<div class="alert alert-danger">
              No city found or location access denied
              </div>`;
          }
        });
      } else {
        const cityFoundMsg = document.querySelector("[data-city-found]");
        cityFoundMsg.innerHTML =
          `<div class="alert alert-danger">Geolocation isn't supported by this browser.</div>`;
      }
    } catch (error) {
      console.error("Error:", error);
      const cityFoundMsg = document.querySelector("[data-city-found]");
      cityFoundMsg.innerHTML =
        `<div class="alert alert-danger">Error fetching information</div>`;
    }
  });