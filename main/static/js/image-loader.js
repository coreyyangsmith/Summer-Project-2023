var calgaryCommunities = {}; // store community data
var communityCode = [];
const imageLeft = $(".image-left");
const imageLeftHeader = $(".left-header");
const imageRight = $(".image-right");
const imageRightHeader = $(".right-header");
const imagePathPrefix = "../../../media/community_images";

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

function loadRandomImage() {
  let min = 0;
  let max = communityCode.length;

  // get random number
  let randomIntLeft = getRandomInt(min, max);
  let randomIntRight = getRandomInt(min, max);

  // get community code based on random number
  let randomCommunityCodeLeft = communityCode[randomIntLeft];
  let randomCommunityCodeRight = communityCode[randomIntRight];

  // get filenames
  let randomImageLeft =
    imagePathPrefix +
    "/" +
    calgaryCommunities[randomCommunityCodeLeft]["filename"];
  let randomImageRight =
    imagePathPrefix +
    "/" +
    calgaryCommunities[randomCommunityCodeRight]["filename"];

  // get community names
  let leftCommunityName = calgaryCommunities[randomCommunityCodeLeft]["name"];
  let rightCommunityName = calgaryCommunities[randomCommunityCodeRight]["name"];

  // change the image
  imageLeft.attr("src", randomImageLeft);
  imageRight.attr("src", randomImageRight);

  // change the txt
  imageLeftHeader.text(leftCommunityName);
  imageRightHeader.text(rightCommunityName);
}

function changeHeader() {}

$.getJSON(
  "../../../media/community_images/utils/communities.json",
  function (data) {
    calgaryCommunities = data;
    communityCode = Object.keys(calgaryCommunities);
    loadRandomImage();
  }
).fail(function (jqXHR, textStatus, errorThrown) {
  console.error("Error loading JSON data:", textStatus, errorThrown);
});
