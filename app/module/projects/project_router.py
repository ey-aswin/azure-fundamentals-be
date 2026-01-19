from fastapi import APIRouter, Depends
from app.db.cosmosdb.containers.projectContainer import get_project_container
from app.module.projects.project_schema import ProjectCreateSchema,ProjectEditSchema

router = APIRouter(prefix="/project", tags=["project"])


@router.post("/create")
def project_status(
    bodyData: ProjectCreateSchema,
    project_container_service=Depends(get_project_container),
):
    items = project_container_service.create_item(bodyData.model_dump())
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
