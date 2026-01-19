from pymongo import MongoClient
from app.config.config import Config    
from fastapi.encoders import jsonable_encoder
from bson import ObjectId



class MongoDB:
    def __init__(self, uri: str, db_name: str):
        self.client = MongoClient(uri)
        self.db = self.client[db_name]

    def get_collection(self, collection_name: str):
        return self.db[collection_name]

    def close(self):
        self.client.close()
        
    def create_item(self, collection_name: str, item: dict):
        collection = self.get_collection(collection_name)
        result = collection.insert_one(item)
        # inserted_id = result.inserted_id
        return {"ok": result.acknowledged, "inserted_id": str(result.inserted_id)}
        # return jsonable_encoder(result, custom_encoder={ObjectId: str})
        # return {"inserted_id": str(inserted_id)}
    
    def read_item(self, collection_name: str, query: dict):
        collection = self.get_collection(collection_name)
        return collection.find_one(query)   
    
    def query_items(self, collection_name: str, query: dict):
        collection = self.get_collection(collection_name)
        items = list(collection.find(query)) 
        return jsonable_encoder(items, custom_encoder={ObjectId: str})
    
 
    def delete_item(self, collection_name: str, query: dict):
        print(query)
        collection = self.get_collection(collection_name)
        return collection.delete_many(query) 

# Singleton MongoDB connection
mongo = ""
# Dependency injection function
def mongo_connection() -> MongoDB:
    return mongo  