from fastapi import HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
from jose import JWTError, jwt

from src.config.settings import settings

class AuthService:
    def __init__(self):
        self.secret_key = settings.SECRET_KEY
        self.algorithm = settings.ALGORITHM
        self.access_token_expire_minutes = settings.ACCESS_TOKEN_EXPIRE_MINUTES
        self.fake_user = {
            "username": settings.FAKE_USERNAME,
            "password": settings.FAKE_PASSWORD
        }

    def fake_login(self):
        access_token_expires = timedelta(minutes=self.access_token_expire_minutes)
        access_token = self.create_access_token(data={"sub": self.fake_user["username"]}, expires_delta=access_token_expires)
        return {"access_token": access_token, "token_type": "bearer"}

    def login(self, form_data: OAuth2PasswordRequestForm = Depends()):
        # Aquí iría la lógica real de autenticación con base de datos
        # user = get_user_from_db(form_data.username)
        # if not user or not verify_password(form_data.password, user.hashed_password):
        #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
        raise HTTPException(status_code=status.HTTP_501_NOT_IMPLEMENTED, detail="DB authentication not implemented")


    def create_access_token(self, data: dict, expires_delta: timedelta):
        to_encode = data.copy()
        expire = datetime.utcnow() + expires_delta
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, self.secret_key, algorithm=self.algorithm)
        return encoded_jwt

    def get_current_user(self, token: str = Depends()):
        credentials_exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            username: str = payload.get("sub")
            if username is None:
                raise credentials_exception
        except JWTError:
            raise credentials_exception
        return username


auth_service = AuthService()
