from azure.cosmos import CosmosClient
import uuid
from datetime import datetime,timedelta


class CosmosDBService:
    def __init__(self, connection_string, database_name, container_name,partition_key):
        self.client = CosmosClient.from_connection_string(connection_string)
        self.database_name = database_name
        self.container_name = container_name
        self.database = self.client.get_database_client(database_name)
        self.container = self.database.get_container_client(container_name)
        self.partition_key = "react-demo" 
    def create_item(self, item):
        bodyItems={**item,"test": "react-demo","id": str(uuid.uuid4()),"created_at": str(datetime.utcnow())}
        return self.container.create_item(body=bodyItems)   
        
    def upload_item(self, item):
        bodyItems={**item,"test": "react-demo","created_at": str(datetime.utcnow())}
        return self.container.upsert_item(body=bodyItems) 
    
    def read_item(self, database_name, container_name, item_id, partition_key):
        return self.container.read_item(item=item_id, partition_key=partition_key)   

    def query_items(self, query, parameters):
        return list(self.container.query_items(
            query=query,
            parameters=parameters,
            enable_cross_partition_query=True
        ))
    def delete_item(self,item_id):
        print(item_id)
        return self.container.delete_item(item=item_id, partition_key=self.partition_key)     
