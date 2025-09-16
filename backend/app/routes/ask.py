from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import Course
import re

router = APIRouter()

@router.post("/ask")
def ask_ai(question: dict, db: Session = Depends(get_db)):
    q = question.get("question", "").lower()

    filters = {}

    # 🎯 Rule-based parsing

    # 1) Level (UG / PG)
    if "ug" in q or "undergraduate" in q:
        filters["level"] = "UG"
    elif "pg" in q or "postgraduate" in q:
        filters["level"] = "PG"

    # 2) Delivery Mode
    if "online" in q:
        filters["delivery_mode"] = "online"
    elif "offline" in q:
        filters["delivery_mode"] = "offline"
    elif "hybrid" in q:
        filters["delivery_mode"] = "hybrid"

    # 3) Department (basic keyword match)
    departments = ["computer science", "mathematics", "physics", "chemistry", "business", "economics"]
    for dept in departments:
        if dept in q:
            filters["department"] = dept.title()

    # 4) Fee cap
    fee_match = re.search(r"under (\d+)", q)
    if fee_match:
        filters["max_fee"] = int(fee_match.group(1))

    # Query DB with parsed filters
    query = db.query(Course)

    if "level" in filters:
        query = query.filter(Course.level == filters["level"])
    if "delivery_mode" in filters:
        query = query.filter(Course.delivery_mode == filters["delivery_mode"])
    if "department" in filters:
        query = query.filter(Course.department == filters["department"])
    if "max_fee" in filters:
        query = query.filter(Course.tuition_fee_inr <= filters["max_fee"])

    results = query.all()

    if not results:
        return {
            "parsed_filters": filters,
            "message": "No matching courses found"
        }

    return {
        "parsed_filters": filters,
        "results": results
    }

