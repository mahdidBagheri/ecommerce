from datetime import datetime, timedelta

from . import schema

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

SERCRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHEM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTS = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SERCRET_KEY, algorithm=ALGORITHEM)
    return encoded_jwt

def veriffy_token(token: str, credentials_exception):
    try:
        payload = jwt.decode(token, SERCRET_KEY, algorithms=[ALGORITHEM])
        email: str = payload.get("sub")
        if email is None:
            raise credentials_exception
        token_data = schema.TokenData(email=email)
        return token_data
    except JWTError:
        raise credentials_exception

oauth2_schema = OAuth2PasswordBearer(tokenUrl="login")

def get_current_user(data:str = Depends(oauth2_schema)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="unautherized",
        headers={"WWW=Authenticate": "Bearer"}
    )
    return veriffy_token(data, credentials_exception)