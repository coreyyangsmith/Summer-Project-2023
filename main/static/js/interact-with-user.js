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
  ajax_update(comm_code);
  loadRandomImage();
});

$(".image-right").click(function () {
  comm_code = document.getElementById("img-right").src.split("/").pop().split(".")[0]
  ajax_update(comm_code);
  loadRandomImage();
});


function ajax_update(comm_code) {
  console.log("running ajax update");
  console.log("received comm: " + comm_code);

  $.ajax({
      type: 'GET',
      url: "vote/" + comm_code,
      data: {"comm_code": comm_code},
      success: function (comm_code) {
        console.log("User voted for: " + comm_code)
      },
      error: function (response) {
          console.log(response)
      }
  })
}

