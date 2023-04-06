//
// navbar
//

const searchForm = document.querySelector(".search-form");
const mobileNav = document.querySelector(".mobile-navbar");
const mobileNavOptions = document.querySelector(".mobile-nav-options");

function searchToggle() {
  searchForm.classList.toggle("open");
  if (searchForm.classList.contains("open")) {
    searchForm.style.transform = "scaleX(1)";
  } else {
    searchForm.style.transform = "scaleX(0)";
  }
}

function menuOpen() {
  mobileNav.classList.add("menu-opened");
}

function menuClose() {
  mobileNav.classList.remove("menu-opened");
}

//
// gallery post
//

const modalImg = document.querySelector(".modal-img img");

let selectedImg = "";

function highlight() {
  window.onclick = (e) => {
    selectedImg = `${e.target.getAttribute("src")}`;
    modalImg.setAttribute("src", selectedImg);
  };
}
