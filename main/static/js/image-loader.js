var calgaryCommunities = {}; // store community data
var communityCode = [];
const imageLeft = $(".image-left");
const imageRight = $(".image-right");
const imagePathPrefix = "../../../media/community_images";

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

function loadRandomImage() {
  let min = 0;
  let max = communityCode.length;
  let randomIntLeft = getRandomInt(min, max);
  let randomIntRight = getRandomInt(min, max);
  let randomImageLeft = imagePathPrefix + communityCode[randomIntLeft] + ".jp";
}

$.getJSON(
  "../../../media/community_images/utils/communities.json",
  function (data) {
    calgaryCommunities = data;
    communityCode = Object.keys(calgaryCommunities);
  }
).fail(function (jqXHR, textStatus, errorThrown) {
  console.error("Error loading JSON data:", textStatus, errorThrown);
});
