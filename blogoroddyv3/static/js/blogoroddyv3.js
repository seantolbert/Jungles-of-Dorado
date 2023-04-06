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
// modal functionality
//

const modal = document.querySelector(".modal");
const modalImg = document.querySelector(".modal-img img");
const dimmer = document.querySelector(".dimmer");
const closeBtn = document.querySelector(".close-modal");

let selectedImg = "";
let selectedLink = "";

function highlight() {
  window.onclick = (e) => {
    selectedImg = e.target.getAttribute("src");
    selectedLink = e.target.getAttribute("alt");
    if (selectedImg !== null) {
      modalImg.setAttribute("src", selectedImg);
    }
  };
  dimmer.style.background = "rgba(0, 0, 0, 0.75)";
  dimmer.style.pointerEvents = "auto";
  closeBtn.style.display = "block";
  modal.style.display = "flex";
}

function closeModal() {
  dimmer.style.background = "transparent";
  dimmer.style.pointerEvents = "none";
  closeBtn.style.display = "none";
  modal.style.display = "none";
}

function instaNavigation() {
  if (selectedLink !== "#" && selectedLink !== "") {
    window.open(selectedLink, "_blank");
  }
}
