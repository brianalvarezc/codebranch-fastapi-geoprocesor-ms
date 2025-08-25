from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from src.config.settings import settings
from src.services.auth_service import auth_service
from src.services.schemas.token_schema import TokenSchema

router = APIRouter()

# Usuario simulado (en producción usar DB)
FAKE_USER = {
    "username": settings.FAKE_USERNAME,
    "password": settings.FAKE_PASSWORD
}

USE_FAKE_USER = str(settings.USE_FAKE_USER).lower() == "true"

oauth2_scheme = OAuth2PasswordBearer(tokenUrl=f"{settings.API_BASE_PATH}/login")

SECRET_KEY = settings.SECRET_KEY
ALGORITHM = settings.ALGORITHM
ACCESS_TOKEN_EXPIRE_MINUTES = settings.ACCESS_TOKEN_EXPIRE_MINUTES

# Autenticación y generación de token
@router.post("/login", response_model=TokenSchema)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if USE_FAKE_USER:
        return auth_service.fake_login()
    else:
        return auth_service.login(form_data)



# Dependencia para proteger endpoints
def get_current_user(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    return username
