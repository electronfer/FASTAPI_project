from typing import Annotated
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from TodoApp.models import Users
from sqlalchemy.orm import Session
from TodoApp.database import SessionLocal
from passlib.context import CryptContext
from starlette import status

router = APIRouter()

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