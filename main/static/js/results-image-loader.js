/**
 * Updates result page images and community names.
 *
 * @version 1.x (testing for functionality)
 *
 * Note (s):
 *    - Uses the following CSS classes:
 *      - image-leaderboard, community-name
 *    - Uses JSON file (s): "../../../media/community_images/utils/communities.json"
 *    - Expecting images under "../../../media/community_images"
 */

// store community names
var calgaryCommunities = {};
var communityCode = [];

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
