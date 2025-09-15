from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, Header
from sqlalchemy.orm import Session
import csv
from ..db import get_db
from .. import models
import os

router = APIRouter()

INGEST_TOKEN = os.getenv("INGEST_TOKEN", "secret123")

@router.post("/")
async def ingest_courses(
    file: UploadFile = File(...),
    x_ingest_token: str = Header(None),
    db: Session = Depends(get_db)
):
    if x_ingest_token != INGEST_TOKEN:
        raise HTTPException(status_code=401, detail="Invalid token")

    reader = csv.DictReader((line.decode("utf-8") for line in file.file))
    inserted = 0
    for row in reader:
        course = models.Course(
            course_name=row["course_name"],
            department=row["department"],
            level=row["level"],
            delivery_mode=row["delivery_mode"],
            credits=int(row["credits"]),
            duration_weeks=int(row["duration_weeks"]),
            rating=float(row["rating"]),
            tuition_fee_inr=int(row["tuition_fee_inr"]),
            year_offered=int(row["year_offered"]),
        )
        db.merge(course)  # insert or update
        inserted += 1
    db.commit()
    return {"message": f"{inserted} courses ingested successfully"}

