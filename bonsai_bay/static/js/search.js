/* 
* Accesses the data attributes for search link and search bar
* Adds a click event on the search, including prevent default.
* Use to toggle to add or remove d-none from the classlist
*/
document.addEventListener('DOMContentLoaded', function () {
  const searchLink = document.querySelector('[data-toggle-search]');
  const searchBar = document.querySelector('[data-search-bar]');

  searchLink.addEventListener('click', function (event) {
    event.preventDefault();
    searchBar.classList.toggle('d-none');
  });
});


/**  searchListings() function: 
* Accesses the search query id from base.html
* Send the search query input as a request parmeter using fetch.
* Gets a json response with the data.
* Clears the listings currently displayed in homepage.
* Iterates through the response data
* Appends newly created item cards with the listings in the response data.
* Log errors to console if issues.
**/

function searchListings() {
  let query = document.getElementById("search-query").value.trim();
  fetch(`/search?query=${query}`)
    .then(response => response.json())
    .then(data => {

      let listingsContainer = document.querySelector(".listings");
      listingsContainer.innerHTML = "";

      data.forEach(listing => {
        let listingDiv = document.createElement("div");
        listingDiv.classList.add("col-10", "col-sm-6", "col-md-4", "col-lg-3");
        listingDiv.innerHTML = `
          <div class="item-card-container">
            <a href="/item/${listing.id}" class="item-card-link">
              <div class="item-card item-card-small">
                <div class="listing">
                  <h6>${listing.title}</h6>
                </div>
                ${listing.image ? `<img src="data:image/jpeg;base64,${listing.image}" alt="${listing.title} Image" style="max-width: 100%; height: auto" class="img-fluid">` : '<p>No image available</p>'}
                <p>&pound;${listing.price}</p>
              </div>
            </a>
          </div>
        `;
        listingsContainer.appendChild(listingDiv);
      });
    })
    .catch(error => console.error('Error:', error));
}
