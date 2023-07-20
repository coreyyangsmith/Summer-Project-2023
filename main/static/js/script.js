function checkURL() {
  if (window.location.pathname.endsWith("index.html")) {
    console.log("index.html is loaded.");
  }
}

$(".image-left").click(function () {
  console.log("image left clicked");
});

$(".image-right").click(function () {
  console.log("image right clicked");
});
