from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from src.config.settings import settings
from src.infrastructure.api.v1 import all_routers

app = FastAPI(
    title=settings.API_TITLE,
    description=settings.API_DESCRIPTION,
    version="1.0.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routes
for router, prefix in all_routers:
    app.include_router(router, prefix=f"{settings.API_BASE_PATH}{prefix}")

@app.get("/")
async def root():
    return {"message": "Bienvenido a la API Geo-procesador"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.app:app", host="0.0.0.0", port=settings.API_PORT, reload=True)
