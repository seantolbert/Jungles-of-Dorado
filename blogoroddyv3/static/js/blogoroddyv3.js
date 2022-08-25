const modal = document.getElementById("modal");

htmx.on("htmx:afterSwap", (e) => {
  if (e.detail.target.id == "dialog") {
    modal.show();
  }
});

htmx.on("htmx:beforeSwap", (e) => {
  if (e.detail.target.id == "dialog" && !e.detail.xhr.response) {
    modal.hide();
    e.detail.shouldSwap = false;
  }
});
