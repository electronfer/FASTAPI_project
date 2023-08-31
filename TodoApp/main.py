from fastapi import FastAPI
from .database import engine, Base
from .routers import admin, auth, todos, users

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(users.router)