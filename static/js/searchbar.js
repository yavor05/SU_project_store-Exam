document.addEventListener('DOMContentLoaded', function() {
  const searchForm = document.getElementById('search-form');
  const searchInput = document.getElementById('search-input');

  searchForm.addEventListener('submit', function(event) {
    event.preventDefault();
    const query = searchInput.value.trim();
    if (query) {
      performSearch(query);
    }
  });

  function performSearch(query) {
    const url = `/search/?q=${encodeURIComponent(query)}`;
    fetch(url)
      .then(response => response.json())
      .then(data => displaySearchResults(data))
      .catch(error => console.error('Error fetching search results:', error));
  }

  function displaySearchResults(results) {
    // Here, you can handle the search results returned from the server.
    // Update your HTML to display the results as needed.
    // For example, you could update a search results container on your page.
    console.log(results);
  }
});
