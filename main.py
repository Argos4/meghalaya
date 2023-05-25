from typing import Union
from typing import List
from fastapi import FastAPI
from pydantic import BaseModel
import validation

class AppProfile(BaseModel):
    app_id : str

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
    common_tags: CommonTags
    capabilities_list: List[str]
    resource_group_name: str
    resource_group_location: str
    azurerm_cosmosdb_account: CosmosDBAccount


app = FastAPI()

@app.get("/")
async def home():
    return {"Welcome to Meghalaya !!"}

@app.post("/build_resource/")
async def build_resource(resource: DataModel):
    if validation.validate_app(resource.app_profile.app_id) == True :
        return {"Input for Cosmos DB": "valid Response"}

    else:
        return {"Response from API": "Invalid Request"}
