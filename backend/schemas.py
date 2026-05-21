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
    project_id: int
    assigned_to: int
    due_date: Optional[date] = None



class StatusUpdate(BaseModel):
    status: str