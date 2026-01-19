from fastapi import APIRouter
from app.module.v2.blobstorage.blobstorage_router import router as blobstorage_router   


router = APIRouter(prefix='/api/v2',tags=['v2'])



@router.get("/status")
def status_check(): 
    return {"status": "API is running successfully."}


# Include blobstorage router
# description: Routes related to blob storage operations
# path: /api/v2/blobstorage/*
router.include_router(blobstorage_router)