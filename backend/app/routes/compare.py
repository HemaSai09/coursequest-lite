from fastapi import APIRouter, Query, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Course

router = APIRouter()

@router.get("/compare")
def compare_courses(ids: str = Query(..., description="Comma-separated course IDs"), db: Session = Depends(get_db)):
    id_list = [cid.strip() for cid in ids.split(",")]

    courses = db.query(Course).filter(Course.course_id.in_(id_list)).all()

    if not courses:
        return {"message": "No matching courses found"}

    return {"courses": courses}

