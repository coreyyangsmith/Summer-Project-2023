var calgaryCommunities = {}; // store community data
var communityCode = [];

$.getJSON("../../../Data/Testing/JSON/communities.json", function (data) {
  calgaryCommunities = data;
  communityCode = Object.keys(calgaryCommunities);
  console.log(communityCode[0]);
  console.log(communityCode.length);
}).fail(function (jqXHR, textStatus, errorThrown) {
  console.error("Error loading JSON data:", textStatus, errorThrown);
});
