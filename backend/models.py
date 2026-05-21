from sqlalchemy import Column, Integer, String,  ForeignKey, Date
from database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(150), unique=True)
    password = Column(String(255))
    role = Column(String(20), default="member")

class Project(Base):
    __tablename__ = "projects"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(200))
    description = Column(String(500))
    created_by = Column(Integer, ForeignKey("users.id"))

    creator = relationship("User")

class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    description = Column(String(500))
    status = Column(String(50), default="pending")

    due_date = Column(Date, nullable=True)

    project_id = Column(Integer, ForeignKey("projects.id"))
    assigned_to = Column(Integer, ForeignKey("users.id"))

    project = relationship("Project")
    user = relationship("User")