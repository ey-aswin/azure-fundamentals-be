from pydantic import BaseModel, Field
from typing import Optional, List


class ProjectCreateSchema(BaseModel):
    # id: str = Field(..., description="Unique identifier for the project")
    # test: str = Field(..., description="TTest key")
    title: str = Field(..., description="Name of the project")
    description: Optional[str] = Field(None, description="Description of the project")
    categories: str = Field(..., description="Category")

class ProjectEditSchema(ProjectCreateSchema):
    id:str = Field(..., description="id of the project")