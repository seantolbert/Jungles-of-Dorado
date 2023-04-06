const searchForm = document.querySelector(".search-form");
const mobileNav = document.querySelector(".mobile-nav");

function searchToggle() {
  searchForm.classList.toggle("open");
  if (searchForm.classList.contains("open")) {
    searchForm.style.transform = "scaleX(1)";
  } else {
    searchForm.style.transform = "scaleX(0)";
  }
}

function menuToggle() {
  console.log(mobileNav);
  mobileNav.classList.toggle("menu-opened");
}
