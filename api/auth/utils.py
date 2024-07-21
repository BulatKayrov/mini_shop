from datetime import datetime, timedelta

import jwt.exceptions
from fastapi import HTTPException, status, Depends
from fastapi.requests import Request
from passlib.context import CryptContext

from .model import UserModel
from config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def authenticate_user(instance, email: str, password: str):
    user = await instance.find_by_email(email=email)

    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found')

    if not verify_password(password, user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid credentials')

    return user


def jwt_encode(payload: dict, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM):
    return jwt.encode(payload=payload, key=key, algorithm=algorithm)


def jwt_decode(token: str, key=settings.SECRET_KEY, algorithm=settings.ALGORITHM):
    return jwt.decode(jwt=token, key=key, algorithms=algorithm)


def get_token(request: Request):
    return request.cookies.get("token")


def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt_encode(payload=to_encode)


async def get_current_user(token=Depends(get_token)):

    if token is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token not found')

    try:
        payload = jwt_decode(token=token)
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Token expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Invalid token')

    email = payload.get("sub")
    return await UserModel.find_by_email(email=email)
