from azure.storage.blob import ContentSettings, ContainerClient,generate_blob_sas,BlobSasPermissions
from app.config.config import Config
from datetime import datetime,timedelta

contianer = ContainerClient.from_connection_string(
    Config.BLOB_STORAGE_CONNECTION_STRING, container_name="blobimages"
)


class BlobStorageAzureContainer:
    def __init__(self):
        self.container_client = contianer 

    def get_blob_url_with_sas(self, blob_name):
        account_name="aswinstorageblob"
        container_name="blobimages"
        account_key=Config.BLOB_STORAGE_KEY  # Replace with your actual account key
        sas_token = generate_blob_sas(
        account_name=account_name,
        container_name=container_name,
        blob_name=blob_name,
        account_key=account_key,
        permission=BlobSasPermissions(read=True),  # read-only access
        expiry=datetime.utcnow() + timedelta(hours=1)  # valid for 1 hour
    )
        blob_url = f"https://{account_name}.blob.core.windows.net/{container_name}/{blob_name}?{sas_token}"
        return blob_url


    def upload_blob(self, blob_name, data, content_type):
        result = self.container_client.upload_blob(
            blob_name,
            data,
            overwrite=True,
            content_settings=ContentSettings(content_type=content_type),
        )
        return result

    def get_all_blobs(self):
        blobList = []
        result = self.container_client.list_blobs()
        for blob in result:
            blobList.append({"blob_item_name":blob.name, "blob_url":self.get_blob_url_with_sas(blob.name)})
        return blobList

    def remove_blob(self,img_id):
        result = self.container_client.delete_blob(img_id   )


# Singleton BlobStorageAzureContainer instance
blob_storage_azure_container = BlobStorageAzureContainer()


def get_blob_storage_azure_container() -> BlobStorageAzureContainer:
    return blob_storage_azure_container
