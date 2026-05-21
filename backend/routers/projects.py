from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Project, User
from schemas import ProjectCreate

router = APIRouter(prefix="/projects", tags=["Projects"])


# DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# CREATE PROJECT (FIXED)
# =========================
@router.post("/")
def create_project(project: ProjectCreate, db: Session = Depends(get_db)):

    # validate user exists
    user = db.query(User).filter(User.id == project.created_by).first()

    if not user:
        raise HTTPException(status_code=400, detail="User not found")

    new_project = Project(
        name=project.name,
        description=project.description,
        created_by=project.created_by
    )

    db.add(new_project)
    db.commit()
    db.refresh(new_project)

    return {
        "message": "Project created successfully",
        "project_id": new_project.id
    }


# =========================
# GET ALL PROJECTS
# =========================
@router.get("/")
def get_projects(db: Session = Depends(get_db)):
    return db.query(Project).all()