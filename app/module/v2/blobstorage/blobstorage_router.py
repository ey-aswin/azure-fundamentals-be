from fastapi import APIRouter, Depends,UploadFile,File
from app.db.blobstorage.storagecontainer_azure import get_blob_storage_azure_container

from app.module.v2.blobstorage.blobstorage_repository import get_blob_repository
router = APIRouter(prefix='/blobstorage',tags=['blobstorage'])

# lowercase and underscore
# Decorators 
# Recursive Function
# Generators
# Yield
# Class - based code works 
# Middleware
# JWT
# Fastapi Config backend
# Authentication
# Schduler
# Background task 
# Web Sockets

# Excel - New Things, Progress, Start/End Date, Comments, Description, Blockers






@router.get("/info")
def blobstorage_info(): 
    return {"info": "Blob Storage Router is operational."}

@router.post("/upload")
async def upload_blobs(file:UploadFile=File(),blobRepo = Depends(get_blob_repository)):
    uploadedBlob = await blobRepo.uploadBlob(file)
    return {"msg": "Blob uploaded successfully.","info":uploadedBlob}


@router.get("/all")
async def get_all_uploaded_files (blobRepo = Depends(get_blob_repository)):
    blob_items =blobRepo.get_all_blob_items()
    return {"msg":"blob list","blob_items":blob_items}



@router.delete("/delete/{img_id}")
async def get_all_uploaded_files (img_id:str,blobRepo = Depends(get_blob_repository)):
    blob_items =blobRepo.remove_blob_item(img_id)
    return {"msg":"blob list","blob_items":blob_items}