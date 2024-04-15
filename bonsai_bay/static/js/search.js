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

/*
Functionality to:
* Access attributes for search form, input and button 
* When pressing enter or click on the search icon button; 
logs input to the console.
*/
document.addEventListener("DOMContentLoaded", function () {
  const searchForm = document.getElementById("searchForm");
  searchForm.addEventListener("submit", function (event) {
    event.preventDefault();
    let searchInput = document.querySelector(".form-control").value;
    console.log("Search query:", searchInput);
  });

  let button = document.querySelector(".search-btn");

  button.addEventListener("click", function (event) {

    event.preventDefault();
    searchForm.dispatchEvent(new Event("submit"));
  });
});