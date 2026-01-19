from dotenv import load_dotenv
import os
load_dotenv()

class Config:
    ENVIRONMENT = os.getenv("ENVIRONMENT", "production")
    DEBUG = ENVIRONMENT == "development"
    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./test.db")
    SECRET_KEY = os.getenv("SECRET_KEY", "your-secret-key")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 300  # 30 hours 
    COSMOS_DB_CONNECTION_STRING = os.getenv("COSMOS_DB_CONNECTION_STRING", "")
    COSMOS_DB_DATABASE_NAME = os.getenv("COSMOS_DB_DATABASE_NAME", "" )
    COSMOS_DB_CONTAINER_NAME = os.getenv("COSMOS_DB_CONTAINER_NAME", "")
    MONGO_DB_URI = os.getenv("MONGO_DB_URI", "")
    MONGO_DATABASE_NAME = os.getenv("MONGO_DATABASE_NAME", "")  
    CORS_HOSTS = os.getenv("CORS_HOSTS", "").split(",")
    BLOB_STORAGE_CONNECTION_STRING = os.getenv("BLOB_STORAGE_CONNECTION_STRING", "")
    BLOB_CONTAINER_NAME = os.getenv("BLOB_STORAGE_CONTAINER_NAME", "")
            


    