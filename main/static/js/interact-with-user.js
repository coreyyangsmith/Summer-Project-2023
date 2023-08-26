/**
 * Interacts with user image clicks
 *
 * Note (s):
 *    - Uses the following css classes:
 *      - image-left, image-right
 *
 * @version 1.0.0
 */

/**
 * Listens for left and right image clicks on home page.
 */
$(".image-left").click(function () {
  comm_code = document.getElementById("img-left").src.split("/").pop().split(".")[0]
  console.log(comm_code);
  loadRandomImage();
});

$(".image-right").click(function () {
  comm_code = document.getElementById("img-right").src.split("/").pop().split(".")[0]
  console.log(comm_code);
  loadRandomImage();
});
