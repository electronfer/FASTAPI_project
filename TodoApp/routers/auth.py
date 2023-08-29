from fastapi import APIRouter
from TodoApp.models import Users
from pydantic import BaseModel
from starlette import status
from passlib.context import CryptContext

router = APIRouter()

bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

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


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(create_user_request: CreateUserRequest):
    
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        last_name=create_user_request.last_name,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True
    )
    
    return create_user_model
    #db.add(create_user_model)
    #db.commit()