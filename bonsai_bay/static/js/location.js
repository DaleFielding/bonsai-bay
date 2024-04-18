/**
* determineCity async function:
* Passes in latitude and longitude coordinates
* Fetches the city name and returns
**/
async function determineCity(latitude, longitude) {
  const response = await fetch(`/get_city/${latitude}/${longitude}`);
  const city = await response.text();
  return city;
}

/**
* Access 'data-get-location' element to add a click event
* Check if geolocation is supported
* If succesful it gets the users position and determines the city
* If city found, updates 'location' element value.
* If not, displays an alerts that says No city found or location access denied.
* Also alerts user if geolocation not supported
* Logs any errors, then alerts "Error fetching information".
**/
document.querySelector('[data-get-location]').addEventListener('click', async function () {
  try {
    if ("geolocation" in navigator) {
      navigator.geolocation.getCurrentPosition(async function (position) {
        const latitude = position.coords.latitude;
        const longitude = position.coords.longitude;
        const city = await determineCity(latitude, longitude);
        if (city) {
          document.getElementById('location').value = city;
        } else {
          alert("No city found or location access denied");
        }
      });
    } else {
      alert("Geolocation is not supported by this browser.");
    }
  } catch (error) {
    console.error('Error:', error);
    alert("Error fetching information");
  }
});