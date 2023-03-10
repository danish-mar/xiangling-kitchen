<?php
// Get the user's search query
$search_query = $_GET['q'];

// Get a list of all the files in the "../rec" directory
$files = scandir('./rec');

// Loop through the files and find any that match the search query
$matches = array();
foreach ($files as $file) {
  if (strpos($file, $search_query) !== false) {
    $matches[] = $file;
  }
}

// Display the matching files on a search results page
echo "<html>";
echo "<head>";
echo "<title>Search Results - Xiangling's Kitchen</title>";
echo "<style>";
echo "body {font-family: Arial, sans-serif; background-color: #f9d5bc;}";
echo "h1 {color: #333; text-align: center;}";
echo ".center { display: flex; justify-content: center; }";
echo "ul {list-style: none;}";
echo "li {margin-bottom: 10px;}";
echo "a {text-decoration: none; color: blue;}";
echo ".xiang_img { display: inline-block; width: 30px; height: 30px; margin-left: 10px; }";
echo "</style>";
echo '<link rel="icon" type="image/png" href="./sticker_5.png">';
echo "</head>";
echo "<body>";
echo "<img src=\"./gouba.png\" alt=\"\" style=\"height: 250px; width: 250px; display: block;margin: 0 auto;\">";
echo "<h1>Xiangling's Kitchen</h1>";
echo "<nav><a href='index.html'>Home</a></nav>";
echo "<h1>Search Results for '$search_query'</h1>";
if (count($matches) == 0) {
  echo "<p>No results found.</p>";
} else {
  echo "<div class='center'>";
  echo "<ul>";
  foreach ($matches as $match) {
    $match_name = substr($match, 0, -5); // remove the extension ".html"
    echo "<li><a href=\"./rec/$match\" target=\"_blank\">$match_name</a>";
    $file_content = file_get_contents("./rec/$match");

    echo "</li>";
  }
  echo "</ul>";
  echo "</div>";
}
echo "</body>";
echo "</html>";
?>
