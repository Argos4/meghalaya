import redis
import json
import worker
def connect_redis():
    redis_client = redis.Redis(host='localhost', port=6379, db=0)
    return  redis_client

def drop_resource_in_redis(resource):
    serialized_data = resource.json()
    redis_client=connect_redis()
    redis_client.set('resource_data', serialized_data)

    serialized_data = redis_client.get('resource_data')

    # Check if the key exists in Redis
    if serialized_data is not None:
        # Deserialize the JSON string back into a Python object
        my_object = json.loads(serialized_data)

        # Print the JSON object
        print ("Below is message from redis")
        print(my_object)
        worker.pull_repository()
        worker.dump_resource_json_file(my_object)
        worker.provision_resource_using_terraform()

    else:
        print("Key not found in Redis.")

