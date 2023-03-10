function search() {
    var keyword = document.getElementById("search-input").value;
    var pages = ["coffee.html", "pancake.html"];
    var results = [];
    for (var i = 0; i < pages.length; i++) {
      var url = "../rec/" + pages[i];
      fetch(url)
        .then(response => response.text())
        .then(data => {
          var doc = new DOMParser().parseFromString(data, "text/html");
          var title = doc.querySelector(".pan_text h1").textContent;
          if (title.toLowerCase().indexOf(keyword.toLowerCase()) !== -1) {
            var imgSrc = doc.querySelector(".img").getAttribute("src");
            results.push({title: title, url: url, imgSrc: imgSrc});
          }
          displayResults(results);
        });
    }
  }
  