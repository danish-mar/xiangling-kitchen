<!DOCTYPE html>
<html>
<head>
	<title>Recipe Search Results</title>
	<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
	<div class="search-container">
		<h1>Recipe Search Results</h1>
		<?php
			$query = $_GET['query'];
			$results = search_recipes($query);
			if (count($results) > 0) {
				foreach ($results as $result) {
					echo '<div class="result-container">';
					echo '<img src="../rec/'.$result['img'].'" alt="'.$result['title'].'">';
					echo '<div class="result-text">';
					echo '<h2>'.$result['title'].'</h2>';
					echo '<p>'.$result['description'].'</p>';
					echo '<a href="../rec/'.$result['file'].'">View Recipe</a>';
					echo '</div>';
					echo '</div>';
				}
			} else {
				echo '<p>No results found for "'.$query.'".</p>';
			}

			function search_recipes($query) {
				$results = array();
				$files = glob('../rec/*.html');
				foreach ($files as $file) {
					$html = file_get_contents($file);
					$doc = new DOMDocument();
					@$doc->loadHTML($html);

					$title = $doc->getElementsByTagName('h1')[0]->nodeValue;
					$description = $doc->getElementsByTagName('meta')[0]->getAttribute('content');
					$img = $doc->getElementsByTagName('img')[0]->getAttribute('src');

					if (stripos($title, $query) !== false || stripos($description, $query) !== false) {
						$results[] = array(
							'title' => $title,
							'description' => $description,
							'img' => $img,
							'file' => basename($file)
						);
					}
				}
				return $results;
			}
		?>
	</div>
</body>
</html>
