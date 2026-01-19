from app.module.v2.v2_api_router import router as v2_api_router
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from .api_router import router as api_router
from app.config.config import Config
from fastapi.middleware.cors import CORSMiddleware


print(f"Starting application in {Config.ENVIRONMENT} mode. Debug={Config.DEBUG}")

app = FastAPI()

origins = [
    *Config.CORS_HOSTS
]
print("CORS Origins:", origins)
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/hello-world")
def name():
    return {"message": "Hello, World!"}


app.include_router(api_router)

# New Approach with versioned router
app.include_router(v2_api_router)

@app.exception_handler(Exception )
async def global_exception_handler(request, exc):
    return JSONResponse(
        status_code=500,
        content={"message": "An unexpected error occurred.", "error": type(exc).__name__},
    ) 