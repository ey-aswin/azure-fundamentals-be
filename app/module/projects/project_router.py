from fastapi import APIRouter, Depends
from app.db.cosmosdb.containers.projectContainer import get_project_container
from app.module.projects.project_schema import ProjectCreateSchema,ProjectEditSchema
import httpx
from app.config import config

router = APIRouter(prefix="/project", tags=["project"])
 

@router.post("/create")
def project_status(
    bodyData: ProjectCreateSchema,
    project_container_service=Depends(get_project_container),
):
    items = project_container_service.create_item(bodyData.model_dump())

    try:
        httpx.get(
            config.Config.FUNCTION_URL + "/api/emailtrigger?todo_id="+items["id"]  ,timeout=30      ) 
        return "success"
    except Exception as exc:
        print(f"An error occurred while requesting search service: {exc}")
        print("Exception repr:", repr(exc))
    
    return {"status": "successfully inserted", "items": items}


@router.get("/all")
def get_all_projects(project_container_service=Depends(get_project_container)):
    query = "SELECT * FROM c order by c._ts desc"
    parameters = []
    items = project_container_service.query_items(query=query, parameters=parameters)
    return {"projects": items}


@router.delete("/{project_id}")
def get_all_projects(
    project_id: str, project_container_service=Depends(get_project_container)
):
    items = project_container_service.delete_item(project_id)
    return {"msg": "item deleted successfully"}




@router.post("/edit")
def project_edit(
    bodyData: ProjectEditSchema,
    project_container_service=Depends(get_project_container),
):
    items = project_container_service.upload_item(bodyData.model_dump())
    return {"status": "successfully inserted", "items": items}
