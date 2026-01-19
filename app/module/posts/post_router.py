from fastapi import APIRouter, Depends
from app.db.cosmosdb.containers.projectContainer import get_project_container
from app.module.projects.project_schema import ProjectCreateSchema
from app.db.mongodb.mongodb import mongo_connection
from bson import ObjectId


router = APIRouter(prefix="/post", tags=["post"])


@router.post("/create")
def project_status(
    bodyData: ProjectCreateSchema,
    mongo_connection=Depends(mongo_connection),
):
    items = mongo_connection.create_item(collection_name="project", item=bodyData.model_dump())
    return {"status": "successfully inserted", "items": items}


@router.get("/all")
def get_all_projects(mongo_connection=Depends(mongo_connection)):
    items = mongo_connection.query_items(collection_name="project", query={})
    return {"projects": items}


@router.delete("/{post_id}")
def get_all_projects(
    post_id: str, mongo_connection=Depends(mongo_connection)
):
    items = mongo_connection.delete_item(collection_name="project", query={"_id": ObjectId(post_id)})
    return {"msg": "item deleted successfully"}
