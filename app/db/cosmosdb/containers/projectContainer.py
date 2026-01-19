from app.db.cosmosdb.cosmosDB   import CosmosDBService
from app.config.config         import Config
# class ProjectContainer(CosmosDBService):

class ProjectContainer(CosmosDBService):
    def __init__(self, container_name: str, db_name: str, connection_string: str,partition_key: str):
        super().__init__(
            connection_string=connection_string,
            database_name=db_name,
            container_name=container_name,
            partition_key=partition_key
        )

# Singleton ProjectContainer instance
projectContainer = ProjectContainer(
    container_name=Config.COSMOS_DB_CONTAINER_NAME,db_name=Config.COSMOS_DB_DATABASE_NAME,
    connection_string=Config.COSMOS_DB_CONNECTION_STRING,partition_key='string') 

def get_project_container() -> ProjectContainer:
    return projectContainer