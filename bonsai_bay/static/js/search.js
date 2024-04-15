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