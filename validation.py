def validate_app(app_id):
    if app_id == "314":
        print("App profile is validated")
        return True
    else:
        return False
def validate_cloud_details(cloud_provider, resource):
    if cloud_provider in ("azure","aws","gcp") and resource in ("cosmosdb"):

        return True
    else:
        return False