const searchForm = document.querySelector(".search-form");
const mobileNav = document.quesrySelector('.mobile-nav')

function searchToggle() {
  searchForm.classList.toggle("open");
  if (searchForm.classList.contains("open")) {
    searchForm.style.transform = "scaleX(1)";
  } else {
    searchForm.style.transform = "scaleX(0)";
  }
}

function menuToggle() {
  
}