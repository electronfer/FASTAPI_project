from fastapi import FastAPI
from .database import engine, Base
from .routers import auth, todos, address

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(address.router)