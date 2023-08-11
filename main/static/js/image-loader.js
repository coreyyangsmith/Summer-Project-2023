var calgaryCommunities = {}; // store community data
var communityCode = [];
const imageLeft = $(".image-left");
const imageRight = $(".image-right");
const imagePathPrefix = "../../../media/community_images";

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function loadRandomImage() {
  let min = 0;
  let max = communityCode.length;
  console.log(max);
  let randomIntLeft = getRandomInt(min, max);
  let randomIntRight = getRandomInt(min, max);

  console.log(randomIntLeft);

  // choose images
  let randomImageLeft = imagePathPrefix + "/" + communityCode[randomIntLeft];
  let randomImageRight = imagePathPrefix + "/" + communityCode[randomIntRight];
}

function changeHeader() {}

$.getJSON(
  "../../../media/community_images/utils/communities.json",
  function (data) {
    calgaryCommunities = data;
    communityCode = Object.key(calgaryCommunities);
    loadRandomImage();
  }
).fail(function (jqXHR, textStatus, errorThrown) {
  console.error("Error loading JSON data:", textStatus, errorThrown);
});
