from pydantic import BaseModel, Field
from typing import Optional

class User(BaseModel):
    username: str
    password: str

class Task(BaseModel):
    title: str
    description: Optional[str] = None
    completed: bool = False
