from typing import Annotated
from fastapi import FastAPI, Depends
import TodoApp.models
from TodoApp.database import engine, SessionLocal
from sqlalchemy.orm import Session
from starlette import status

app = FastAPI()

TodoApp.models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db_dependency = Annotated[Session, Depends(get_db)]

@app.get("/", status_code=status.HTTP_200_OK)
async def read_all(db: db_dependency):
    return db.query(TodoApp.models.Todos).all()