from typing import Optional

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import Task, Project, User
from backend.schemas import TaskCreate, StatusUpdate

router = APIRouter(prefix="/tasks", tags=["Tasks"])


# =========================
# DB SESSION
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# CREATE TASK (SAFE)
# =========================
@router.post("/")
def create_task(task: TaskCreate, db: Session = Depends(get_db)):

    # check project exists
    project = db.query(Project).filter(Project.id == task.project_id).first()
    if not project:
        raise HTTPException(status_code=400, detail="Project not found")

    # check user exists
    user = db.query(User).filter(User.id == task.assigned_to).first()
    if not user:
        raise HTTPException(status_code=400, detail="Assigned user not found")

    new_task = Task(
        title=task.title,
        description=task.description,
        project_id=task.project_id,
        assigned_to=task.assigned_to,
        due_date=task.due_date,
        status="pending"
    )

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return {"message": "Task created successfully", "task_id": new_task.id}

# =========================
# GET TASKS (ROLE BASED)
# =========================
@router.get("/")
def get_tasks(
    role: Optional[str] = None,
    user_id: Optional[int] = None,
    db: Session = Depends(get_db)
):

    if role == "admin":
        return db.query(Task).all()

    if user_id:
        return db.query(Task).filter(Task.assigned_to == user_id).all()

    return db.query(Task).all()

# =========================
# GET TASKS (ROLE BASED)
# =========================


# =========================
# UPDATE TASK STATUS
# =========================
@router.put("/{task_id}")
def update_task(task_id: int, data: StatusUpdate, db: Session = Depends(get_db)):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task.status = data.status

    db.commit()

    return {"message": "Task updated successfully"}

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):

    task = db.query(Task).filter(Task.id == task_id).first()

    if not task:
        return {"error": "Task not found"}

    db.delete(task)
    db.commit()

    return {"message": "Task deleted successfully"}