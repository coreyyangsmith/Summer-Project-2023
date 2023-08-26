/**
 * Updates navbar.
 *
 * @version 1.0.0
 */

/**
 * Based on the current page, set the navbar to active.
 *
 * Note (s):
 *    - Uses the following CSS classes:
 *      - leaderboard-anchor, home-anchor
 *      - li-active
 */
function checkURL() {
  if (window.location.pathname.endsWith("results/")) {
    var resultsElement = $(".leaderboard-anchor");
    resultsElement.addClass("li-active");
  } else if (window.location.pathname.endsWith("/")) {
    var indexElement = $(".home-anchor");
    indexElement.addClass("li-active");
  }
}

checkURL();
