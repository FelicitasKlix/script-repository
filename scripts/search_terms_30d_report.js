var yourEmail = "";

minImpressions = 0;
minConversions = 0;

var fullCleanLog = ""; // initialise fullCleanLog
var keywordCount = 0; // intialise keyword count

function main() {  
  
    var report = AdWordsApp.report(
      "SELECT Query, Conversions, Cost, AdGroupId, QueryTargetingStatus,"
      + " CampaignStatus, AdGroupStatus, CampaignName, AdGroupName, Impressions,"
      + " Clicks, Ctr, ConversionRate, CostPerConversion, ConversionValue,"
      + " QueryMatchTypeWithVariant, KeywordTextMatchingQuery, AverageCpc"
      + " FROM SEARCH_QUERY_PERFORMANCE_REPORT"
      + " WHERE Conversions > "  + minConversions
      + " AND QueryTargetingStatus = 'NONE' AND"
      + " CampaignStatus = 'ENABLED' AND AdGroupStatus = 'ENABLED'"
      + " AND Impressions > " + minImpressions
      + " AND KeywordTextMatchingQuery DOES_NOT_CONTAIN 'URL=='"
      + " AND KeywordTextMatchingQuery DOES_NOT_CONTAIN 'CATEGORY=='"
      + " AND KeywordTextMatchingQuery != '*'"
      + " AND CampaignName DOES_NOT_CONTAIN_IGNORE_CASE 'broad'"
      + " AND CampaignName DOES_NOT_CONTAIN_IGNORE_CASE 'bmm'"
      + " AND CampaignName DOES_NOT_CONTAIN_IGNORE_CASE 'phrase'"
      + " AND CampaignName DOES_NOT_CONTAIN_IGNORE_CASE 'exact'"
      + " AND AdGroupName DOES_NOT_CONTAIN_IGNORE_CASE 'broad'"
      + " AND AdGroupName DOES_NOT_CONTAIN_IGNORE_CASE 'bmm'"
      + " AND AdGroupName DOES_NOT_CONTAIN_IGNORE_CASE 'phrase'"
      + " AND AdGroupName DOES_NOT_CONTAIN_IGNORE_CASE 'exact'"
      + " DURING LAST_30_DAYS"
    );
  
    var searchTerms = createDict(report);
  
    getSearchTerms(searchTerms, report);
  
    Logger.log(searchTerms);
    
    sendEmailWithTable(searchTerms, yourEmail);
    
    
  }

function sendEmailWithTable(searchTerms, yourEmail) {

  
  const subject = "Search Terms Report (last 30 days)";

  let body = "";

  for (const key in searchTerms) {
    body += `<h2>${key}</h2>`;
    body += "<table>";
    body += "<tr><th>searchTerm</th><th>Cost</th><th>Impressions</th><th>Clicks</th><th>Conversions</th></tr>";

    for (const item of searchTerms[key]) {
      body += "<tr>";
      body += `<td>${item.searchTerm}</td>`;
      body += `<td>${item.Cost}</td>`;
      body += `<td>${item.Impressions}</td>`;
      body += `<td>${item.Clicks}</td>`;
      body += `<td>${item.Conversions}</td>`;
      body += "</tr>";
    }

    body += "</table>";
    body += "<br><br>";
  }

  MailApp.sendEmail(yourEmail, subject, "", { htmlBody: body });
}

function getSearchTerms(searchTerms, report){

    var rows = report.rows();
  
    while (rows.hasNext()) {

      var row = rows.next();
      searchTerms[row["CampaignName"]+'|'+row["AdGroupName"]].push({'searchTerm': row["Query"], 'Cost': row["Cost"], 'Impressions': row["Impressions"], 'Clicks': row["Clicks"], 'Conversions': row["Conversions"]});
      //Logger.log(row);
    }
    //return searchTerms;
}


function createDict(report){
    var searchTerms = {};
    var rows = report.rows();
  
    while (rows.hasNext()) {

      var row = rows.next();
      searchTerms[row["CampaignName"]+'|'+row["AdGroupName"]] = []
      //Logger.log(row);
    }
    return searchTerms;
}

// Gets the report at either campaign or ad group level of search queries which:
// - have at least the minimum threshold of conversions
// - are not currently being targeted in the account
// - are in enabled ad groups and campaigns
// - have at least the minimum threshold of impressions
function gimmeMyReport(level, matchType) {
  if (level.toLowerCase() == "campaign") {
    reportLevel = "CampaignName";
  } else if (level.toLowerCase() == "ad group") {
    reportLevel = "AdGroupName";
  }
  cleanLog("Level: " + level + ". Match Type: " + matchType);

  var report = AdWordsApp.report(
    "SELECT Query, Conversions, Cost, AdGroupId, QueryTargetingStatus,"
    + " CampaignStatus, AdGroupStatus, CampaignName, AdGroupName, Impressions,"
    + " Clicks, Ctr, ConversionRate, CostPerConversion, ConversionValue,"
    + " QueryMatchTypeWithVariant, KeywordTextMatchingQuery, AverageCpc"
    + " FROM SEARCH_QUERY_PERFORMANCE_REPORT"
    + " WHERE Conversions > "  + minConversions
    + " AND QueryTargetingStatus = 'NONE' AND"
    + " CampaignStatus = 'ENABLED' AND AdGroupStatus = 'ENABLED'"
    + " AND Impressions > " + minImpressions
    + " AND KeywordTextMatchingQuery DOES_NOT_CONTAIN 'URL=='"
    + " AND KeywordTextMatchingQuery DOES_NOT_CONTAIN 'CATEGORY=='"
    + " AND KeywordTextMatchingQuery != '*'"
    + " AND " + reportLevel + " CONTAINS_IGNORE_CASE '" + matchType + "'"
  );

  return report;
}

function cleanLog(input) {
  Logger.log(input);
  fullCleanLog += "\n" + input;
}