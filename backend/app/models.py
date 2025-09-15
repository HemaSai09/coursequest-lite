from sqlalchemy import Column, Integer, String, Float
from .db import Base

class Course(Base):
    __tablename__ = "courses"

    course_id = Column(Integer, primary_key=True, index=True)
    course_name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    level = Column(String, nullable=False)  # UG / PG
    delivery_mode = Column(String, nullable=False)  # online / offline / hybrid
    credits = Column(Integer)
    duration_weeks = Column(Integer)
    rating = Column(Float)
    tuition_fee_inr = Column(Integer)
    year_offered = Column(Integer)

