function checkURL() {
  if (window.location.pathname.endsWith("results/")) {
    // set leaderboard as active
    var resultsElement = $(".leaderboard-anchor");
    resultsElement.addClass("li-active");
  } else if (window.location.pathname.endsWith("/")) {
    // set home active
    var indexElement = $(".home-anchor");
    indexElement.addClass("li-active");
  }
}

$(".image-left").click(function () {
  console.log("image left clicked");
});

$(".image-right").click(function () {
  console.log("image right clicked");
});

checkURL();
