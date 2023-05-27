from typing import Union
from fastapi import FastAPI
from resourcemodel import DataModel
import validation
import redisoperations


app = FastAPI()

@app.get("/")
async def home():
    return {"Welcome to Meghalaya !!"}

@app.post("/build_resource/")
async def build_resource(resource: DataModel):
    if validation.validate_app(resource.app_profile.app_id) == True \
            and validation.validate_cloud_details(resource.cloud_details.cloud_provider,resource.cloud_details.resource):
        redisoperations.drop_resource_in_redis(resource)

        return {"Input for Cosmos DB": "valid Response"}

    else:
        return {"Response from API": "Invalid Request; check cloud_details and app id details are correct"}
