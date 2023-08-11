var calgaryCommunities = {}; // store community data
var communityPictures = [];
const imageLeft = $(".image-left");
const imageRight = $(".image-right");
const imagePathPrefix = "../../../media/community_images";

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function loadRandomImage() {
  let min = 0;
  let max = communityPictures.length;
  console.log(max);
  let randomIntLeft = getRandomInt(min, max);
  let randomIntRight = getRandomInt(min, max);

  console.log(randomIntLeft);

  // choose images
  let randomImageLeft =
    imagePathPrefix + "/" + communityPictures[randomIntLeft];
  let randomImageRight =
    imagePathPrefix + "/" + communityPictures[randomIntRight];

  // load image
  imageLeft.attr("src", randomImageLeft);
  imageRight.attr("src", randomImageRight);
}

$.getJSON(
  "../../../media/community_images/utils/communities.json",
  function (data) {
    calgaryCommunities = data;
    communityPictures = Object.values(calgaryCommunities);
    loadRandomImage();
  }
).fail(function (jqXHR, textStatus, errorThrown) {
  console.error("Error loading JSON data:", textStatus, errorThrown);
});
