
const searchBox = document.querySelector('.search-box');
const searchForm = searchBox.querySelector('form');
const searchInput = searchForm.querySelector('input');
const searchButton = searchForm.querySelector('button');

searchBox.addEventListener('mouseenter', () => {
  searchForm.classList.add('active');
});

searchBox.addEventListener('mouseleave', () => {
  searchForm.classList.remove('active');
});

searchForm.addEventListener('submit', (e) => {
  e.preventDefault();
  const searchTerm = searchInput.value.trim();
  // Perform search action here
});

