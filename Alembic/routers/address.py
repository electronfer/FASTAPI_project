import sys
sys.path.append("..")

from typing import Optional, Annotated
from fastapi import Depends, APIRouter, HTTPException
from ..models import Address, Users
from ..database import SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel, Field
from .auth import get_current_user

router = APIRouter(
    prefix="/address",
    tags=["address"]
)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]
user_dependency = Annotated[dict, Depends(get_current_user)]

class AddressRequest(BaseModel):
    
    address1: str = Field(min_length=1)
    address2: str = Field(min_length=1)
    city: str = Field(min_length=1)
    state: str = Field(min_length=1)
    country: str = Field(min_length=1)
    postalcode: str = Field(min_length=1)
    apt_num: int = Optional[int]

    class Config:
        json_schema_extra = {
            'example': {
                'address1': 'address1',
                'address2': 'address2',
                'city': 'city',
                'state': 'state',
                'country': 'country',
                'postalcode': 'postalcode',
                'apt_num': 123
            }
        }


@router.post("/")
async def create_address(address: AddressRequest,
                         user: user_dependency,
                         db: db_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail='Authentication Failed')
    
    address_model = Address()
    address_model.address1 = address.address1
    address_model.address2 = address.address2
    address_model.city = address.city
    address_model.state = address.state
    address_model.country = address.country
    address_model.postalcode = address.postalcode
    address_model.apt_num = address.apt_num

    db.add(address_model)
    db.flush()

    user_model = db.query(Users).filter(Users.id == user.get("id")).first()

    user_model.address_id = address_model.id

    db.add(user_model)

    db.commit()

    db.commit()