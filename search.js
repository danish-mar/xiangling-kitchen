// Get the search input field and create a new div for the search suggestions
var search_input = document.querySelector('input[name="q"]');
var suggestions_div = document.createElement('div');
suggestions_div.classList.add('search-suggestions');
search_input.parentNode.insertBefore(suggestions_div, search_input.nextSibling);

// Listen for changes to the search input field
search_input.addEventListener('input', function() {
  // Get the user's search query
  var search_query = search_input.value;

  // Clear any previous search suggestions
  suggestions_div.innerHTML = '';

  // Get a list of all the files in the "../rec" directory
  var files = <?php echo json_encode(glob('./rec/*.html')); ?>;

  // Loop through the files and find any that contain the user's search query
  var matches = [];
  for (var i = 0; i < files.length; i++) {
    if (files[i].indexOf(search_query) !== -1) {
      matches.push(files[i]);
    }
  }

  // Display the search suggestions
  for (var i = 0; i < matches.length; i++) {
    var suggestion = document.createElement('div');
    suggestion.classList.add('search-suggestion');
    suggestion.innerHTML = '<a href="' + matches[i] + '">' + matches[i].replace(/^.*[\\\/]/, '').replace('.html', '') + '</a>';
    suggestions_div.appendChild(suggestion);
  }
});
