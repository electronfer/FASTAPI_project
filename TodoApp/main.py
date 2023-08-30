from fastapi import FastAPI
import TodoApp.models as models
from TodoApp.database import engine
from TodoApp.routers import admin, auth, todos

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)