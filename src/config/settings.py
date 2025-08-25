from typing import List, Optional, Any
from pydantic import field_validator
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    API_TITLE: str = "Geo-procesador API"
    API_DESCRIPTION: str = "Microservicio para procesar coordenadas geográficas."
    PROJECT_NAME: str = "Geo-procesador API"
    API_BASE_PATH: str = "/api/v1"
    API_PORT: int = 8000
    
    # CORS
    CORS_ORIGINS: List[str] = ["*"]
    
    # JWT
    SECRET_KEY: str = "your-secret-key-change-in-production"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    FAKE_USERNAME: str = "admin"
    FAKE_PASSWORD: str = "admin123"
    USE_FAKE_USER: bool = True  # Cambiar a False en producción
    
    # Database
    DATABASE_USER: str = "user"
    DATABASE_PASSWORD: str = "password"
    DATABASE_HOST: str = "localhost"
    DATABASE_PORT: str = "3306"
    DATABASE_DB: str = "geoprocessor"
    SQLALCHEMY_DATABASE_URI: Optional[str] = None

    @field_validator("SQLALCHEMY_DATABASE_URI", mode="before")
    def assemble_db_connection(cls, v: Optional[str], info) -> Any:
        if isinstance(v, str):
            return v
        data = info.data
        return (
            f"mysql+pymysql://{data['DATABASE_USER']}:{data['DATABASE_PASSWORD']}"
            f"@{data['DATABASE_HOST']}:{data['DATABASE_PORT']}/{data['DATABASE_DB']}"
        )
    

    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings()
