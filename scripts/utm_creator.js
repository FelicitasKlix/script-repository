function main(){
    let adGroups = AdsApp.adGroups().withCondition("CampaignStatus = ENABLED").get();
    while (adGroups.hasNext()) {
        let adGroup = adGroups.next();
        let group=adGroup.getName().replace(/\s/g,'_');
        let campaign=adGroup.getCampaign().getName().replace(/\s/g,'_');
        adGroup.urls().setCustomParameters({adgroup: group, campaign: campaign});
    }
}