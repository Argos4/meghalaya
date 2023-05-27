from pydantic import BaseModel
from typing import List

class AppProfile(BaseModel):
    app_id : str

class CloudDetails(BaseModel):
    cloud_provider: str
    resource: str

class CommonTags(BaseModel):
    business_unit: str
    environment: str
    app: str

class CosmosDBAccount(BaseModel):
    azurerm_cosmosdb_account_name: str
    azurerm_cosmosdb_account_offertype: str
    azurerm_cosmosdb_account_kind: str

class DataModel(BaseModel):
    app_profile: AppProfile
    cloud_details: CloudDetails
    common_tags: CommonTags
    capabilities_list: List[str]
    resource_group_name: str
    resource_group_location: str
    azurerm_cosmosdb_account: CosmosDBAccount