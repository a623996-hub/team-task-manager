from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import SessionLocal
from backend.models import User

router = APIRouter(prefix="/users", tags=["Users"])

# DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# GET ALL USERS
@router.get("/")
def get_users(db: Session = Depends(get_db)):
    users = db.query(User).all()
    return users