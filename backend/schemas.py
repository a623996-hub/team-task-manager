from pydantic import BaseModel
from datetime import date
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    role: str


class LoginRequest(BaseModel):
    email: str
    password: str

class ProjectCreate(BaseModel):
    name: str
    description: str
    created_by: int

class TaskCreate(BaseModel):
    title: str
    description: str
    due_date: Optional[str] = None
    project_id: int
    assigned_to: int
   



class StatusUpdate(BaseModel):
    status: str