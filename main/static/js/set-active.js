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

checkURL(); // check the url to set active nav link
