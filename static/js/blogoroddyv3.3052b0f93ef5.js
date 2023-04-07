const searchForm = document.getElementById("search-form");

function searchToggle() {
  searchForm.classList.toggle("open");

  if (searchForm.classList.contains("open")) {
    searchForm.style.transform = "scaleX(1)";
  } else {
    searchForm.style.transform = "scaleX(0)";
  }
}
