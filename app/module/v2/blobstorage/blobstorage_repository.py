
from fastapi import Depends,UploadFile
from app.db.blobstorage.storagecontainer_azure import get_blob_storage_azure_container,BlobStorageAzureContainer
import uuid 

class BlobstorageRepository:
    def __init__(self, blob_service: BlobStorageAzureContainer):
        self.blob_service = blob_service

    async def uploadBlob(self, file: UploadFile):
        blob_name = f"{uuid.uuid4()}_{file.filename}"
        blob_data =await file.read()
        content_type = file.content_type
        # return True
        uploadedBlob = self.blob_service.upload_blob(blob_name=blob_name, data=blob_data, content_type=content_type)
        return {
            "blob_name":  blob_name,
            "content_type": content_type,
            "size_bytes": len(blob_data),
        }

    def get_all_blob_items(self) :
        blob_list =self.blob_service.get_all_blobs()
        return blob_list

    def remove_blob_item(self,img_id):
        blob_item = self.blob_service.remove_blob(img_id)
        return blob_item

# Dependency Injection function
def get_blob_repository(blob_service: BlobStorageAzureContainer = Depends(get_blob_storage_azure_container)) -> BlobstorageRepository:
    return BlobstorageRepository(blob_service)
