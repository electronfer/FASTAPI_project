from typing import Annotated
from datetime import datetime, timedelta
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from TodoApp.models import Users
from sqlalchemy.orm import Session
from TodoApp.database import SessionLocal
from passlib.context import CryptContext
from starlette import status
from fastapi.security import OAuth2PasswordRequestForm
from jose import jwt, JWTError
import os

router = APIRouter()


# generate a secret key: 
# openssl rand -hex 32
SECRET_KEY = os.getenv("SECRET_KEY", '0c603f5b39861eb04765b8cc1139d8a001aa5bd14257753f6806226fd3e1dfe9')
ALGORITHM = 'HS256'


bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]


class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
    role: str

    class Config:
        json_schema_extra = {
            'example': {
                'username': 'user 1',
                'email': 'user.1@example.com',
                'first_name': "user",
                'last_name': "one",
                'password': "user.1",
                'role': "admin"
            }
        }

class Token(BaseModel):
    access_token: str
    token_type: str

def authenticate_user(username: str, password: str, db):
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user


def create_access_token(username: str, user_id: int, role: str, expires_delta: timedelta):
    encode = {'sub': username, 'id': user_id, 'role': role}
    expires = datetime.utcnow() + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)


@router.post("/auth", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )

    db.add(create_user_model)
    db.commit()

@router.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                                 db: db_dependency):
    
    user = authenticate_user(form_data.username, form_data.password, db)

    if not user:
        return 'Failed Authentication'
    
    token = create_access_token(user.username, user.id, user.role, timedelta(minutes=20))

    return {'access_token': token, 'token_type': 'bearer'}
    