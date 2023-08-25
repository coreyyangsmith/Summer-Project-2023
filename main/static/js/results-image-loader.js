/**
 * Updates result page images and community names.
 *
 * @version 1.x (testing for functionality)
 *
 * Note (s):
 *    - Uses the following CSS classes:
 *      - community-name-[ID], community-image-[ID]
 *    - Uses JSON file (s): "../../../media/community_images/utils/communities.json"
 *    - Expecting images under "../../../media/community_images"
 */

// store community names
var calgaryCommunities = {};

// HTML elements
var communityImage;
var communityName;
var communityRank;

// path prefix for images
var imagePathPrefix = "../../../media/community_images";

/**
 * Updates leaderboard page based on unique ID.
 */
function updateLeaderboardPage() {
  communityCodes.forEach((communityCode, index) => {
    let imageFilepath =
      imagePathPrefix + "/" + calgaryCommunities[communityCode]["filename"];
    let communityFullName = calgaryCommunities[communityCode]["name"];

    communityRank = index + 1;
    communityImage = $("#community-image-" + communityRank);
    communityName = $("#community-name-" + communityRank);

    communityName.text(communityFullName);
    console.log(communityName);
    console.log(communityFullName);
    communityImage.attr("src", imageFilepath);
  });
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
    updateLeaderboardPage();
  }
).fail(function (jqXHR, textStatus, errorThrown) {
  console.error("Error loading JSON data:", textStatus, errorThrown);
});
