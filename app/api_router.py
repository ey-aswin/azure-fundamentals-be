from fastapi import APIRouter
from app.module.projects.project_router import router as project_router
from app.module.posts.post_router import router as post_router


router = APIRouter(prefix='/api/v1',tags=['v1'])

# Include project router
# Path: /api/v1/project/*
# description: Routes related to project operations
router.include_router(project_router)


# Include post router
# Path: /api/v1/post/*
# description: Routes related to post operations
# router.include_router(post_router)