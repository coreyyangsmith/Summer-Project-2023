function checkURL() {
  if (window.location.pathname.endsWith("results/")) {
    const resultsElement = document.querySelector(".leaderboard-anchor");
    resultsElement.classList.add("li-active");

    console.log("results.html is loaded");
  } else if (window.location.pathname.endsWith("/")) {
    const indexElement = document.querySelector(".home-anchor");
    indexElement.classList.add("li-active");

    console.log("index.html is loaded.");
  }
}

$(".image-left").click(function () {
  console.log("image left clicked");
});

$(".image-right").click(function () {
  console.log("image right clicked");
});

checkURL();
