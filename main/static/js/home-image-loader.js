/**
 * Loads left and right images for home page.
 *
 * @version 1.x (testing for functionality)
 *
 * Note (s):
 *    - Uses the following CSS classes:
 *      - image-left, image-right
 *      - left-header, right-header
 *    - Uses JSON file (s): "../../../media/community_images/utils/communities.json"
 *    - Expecting images under "../../../media/community_images"
 */

// store community names
var calgaryCommunities = {};
var communityCode = [];

// html elements
const imageLeft = $(".image-left");
const imageLeftHeader = $(".left-header");
const imageRight = $(".image-right");
const imageRightHeader = $(".right-header");

// path prefix for images
const imagePathPrefix = "../../../media/community_images";

/**
 * Generates random number
 *
 * @param {number} min - Minimum range of maximum number
 * @param {number} max - Maximum range of maximum number
 * @returns {number} Random number given a specified range
 */
function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min + 1)) + min;
}

/***
 * Change left and right images on home page
 */
function loadRandomImage() {
  let min = 0;
  let max = communityCode.length;
  let randomIntLeft = getRandomInt(min, max);
  let randomIntRight = getRandomInt(min, max);

  // get community code based on random number
  let randomCommunityCodeLeft = communityCode[randomIntLeft];
  let randomCommunityCodeRight = communityCode[randomIntRight];

  changeImage(randomCommunityCodeLeft, randomCommunityCodeRight);
  changeHeader(randomCommunityCodeLeft, randomCommunityCodeRight);
}

/**
 * Changes left and right images on home page.
 *
 * @param {string} communityCodeLeft - Calgary Community Code
 * @param {string} communityCodeRight - Calgary Community Code
 */
function changeImage(communityCodeLeft, communityCodeRight) {
  let imageLeft =
    imagePathPrefix + "/" + calgaryCommunities[communityCodeLeft]["filename"];
  let imageRight =
    imagePathPrefix + "/" + calgaryCommunities[communityCodeRight]["filename"];

  // change the image
  imageLeft.attr("src", imageLeft);
  imageRight.attr("src", imageRight);
}

/**
 * Changes left and right headers on home page associated to community image.
 *
 * @param {string} communityCodeLeft - Calgary Community Code
 * @param {string} communityCodeRight - Calgary Community Code
 */
function changeHeader(communityCodeLeft, communityCodeRight) {
  let leftCommunityName = calgaryCommunities[communityCodeLeft]["name"];
  let rightCommunityName = calgaryCommunities[communityCodeRight]["name"];

  // change header
  imageLeftHeader.text(leftCommunityName);
  imageRightHeader.text(rightCommunityName);
}

/**
 * load JSON file for test data
 *
 * @throws {Error} Throws an error if the the json file is not found
 */
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
