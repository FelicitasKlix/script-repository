function main() {

    let ss = SpreadsheetApp.openByUrl('https://docs.google.com/spreadsheets/d/1AedPOiG-tHaaki7eqvjwEKQXP6IHwTc4l5_nnC5-5j4/edit#gid=294419712');          // enter the URL of YOUR sheet over there <—
  
  // no need to touch any code below this line ——————————————————————————
  
    // define commonly used query elements. wrap with spaces for safety
    let impr        = ' metrics.impressions ';
    let clicks      = ' metrics.clicks ';
    let cost        = ' metrics.cost_micros ';
    let conv        = ' metrics.conversions '; 
    let value       = ' metrics.conversions_value '; 
    let allConv     = ' metrics.all_conversions '; 
    let allValue    = ' metrics.all_conversions_value '; 
    let views       = ' metrics.video_views ';
    let cpv         = ' metrics.average_cpv ';
    let segDate     = ' segments.date ';  
    let prodTitle   = ' segments.product_title ';
    let campName    = ' campaign.name ';
    let adgName     = ' ad_group.name ';
    let chType      = ' campaign.advertising_channel_type ';
    let adStatus    = ' ad_group_ad.status ';
    let adPerf      = ' ad_group_ad_asset_view.performance_label ';
    let adType      = ' ad_group_ad_asset_view.field_type ';
    let agId        = ' asset_group.id ';  
    let aId         = ' asset.id ';    
    let adPmaxPerf  = ' asset_group_asset.performance_label ';
    let assetText   = ' asset.text_asset.text ';
    let assetSource = ' asset.source ' ; 
    let adUrl       = ' asset.image_asset.full_size.url ';
    let youtubeTitle = ' asset.youtube_video_asset.youtube_video_title ';
    let youtubeId   = ' asset.youtube_video_asset.youtube_video_id ';
    let assetType   = ' asset_group_asset.field_type ';
    let agStrength  = ' asset_group.ad_strength ';
    let agStatus    = ' asset_group.status ';
    let aIdCamp     = ' segments.asset_interaction_target.asset ';
    let interAsset  = ' segments.asset_interaction_target.interaction_on_this_asset '
    let aIdAsset    = ' asset.resource_name ';
    let asgName     = ' asset_group.name ';
    let lgType      = ' asset_group_listing_group_filter.type ';
    let pMaxOnly    =        ' AND campaign.advertising_channel_type = "PERFORMANCE_MAX" '; 
    let searchOnly  =        ' AND campaign.advertising_channel_type = "SEARCH" ';   
    let agFilter    =        ' AND asset_group_listing_group_filter.type != "SUBDIVISION" ';   
    let adgEnabled  = ' AND ad_group.status = "ENABLED" AND campaign.status = "ENABLED" AND ad_group_ad.status = "ENABLED" ';
    let asgEnabled  = ' asset_group.status = "ENABLED" AND campaign.status = "ENABLED" ';           
    let notInter    = ' AND segments.asset_interaction_target.interaction_on_this_asset != "TRUE" '
    let date07      = ' segments.date DURING LAST_7_DAYS '  
    let date30      = ' segments.date DURING LAST_7_DAYS '  
    let order       = ' ORDER BY campaign.name'; 
    
    
    
    // build queries  
    let cd = [segDate, campName, cost, conv, value, views, cpv, impr, clicks, chType] // campaign by day
    let campQuery = 'SELECT ' + cd.join(',') + 
        ' FROM campaign ' +
        ' WHERE ' + date30 + pMaxOnly + order ; 
    
    let dv = [segDate, campName, aIdCamp, cost, conv, value, views, cpv, impr, chType, interAsset] // inter by day
    let dvQuery = 'SELECT ' + dv.join(',') + 
        ' FROM campaign ' +
        ' WHERE ' + date30 + pMaxOnly + notInter + order ; 
    
    let p = [campName, prodTitle, cost, conv, value, impr, chType] // product totals 
    let pQuery = 'SELECT ' + p.join(',')  + 
        ' FROM shopping_performance_view  ' + 
        ' WHERE ' + date30 + pMaxOnly + order ; 
    
    let ag = [segDate, campName, asgName, agStrength, agStatus, lgType, impr, clicks, cost, conv, value] // asset group by day
    let agQuery = 'SELECT ' + ag.join(',')  + 
        ' FROM asset_group_product_group_view ' +
        ' WHERE ' + date30 + agFilter
  
    let ads = [campName, asgName, agId, aIdAsset, assetType, adPmaxPerf, agStrength, agStatus, assetSource] // pMax ads
    let adsQuery = 'SELECT ' + ads.join(',') +
        ' FROM asset_group_asset ' +
        ' WHERE ' + asgEnabled;
   
  
    // call report function to pull data & push to named tabs in the sheet
    runReport(campQuery, ss.getSheetByName('r_camp'));  
    runReport(dvQuery,   ss.getSheetByName('r_dv'));    
    runReport(pQuery,    ss.getSheetByName('r_prod_t')); 
    runReport(agQuery,   ss.getSheetByName('r_ag')); 
    runReport(adsQuery,  ss.getSheetByName('r_ads'));  
  
  }
  
  // query & export report data to named sheet
  function runReport(q,sh) {
    const report = AdsApp.report(q);
    report.exportToSheet(sh);  
  }