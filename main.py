from fastapi import FastAPI
from app.routes import user, tasks

app = FastAPI(title="Smart ToDo API")

app.include_router(user.router)
app.include_router(tasks.router)