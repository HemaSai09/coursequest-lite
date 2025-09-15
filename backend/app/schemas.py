from pydantic import BaseModel

class CourseBase(BaseModel):
    course_name: str
    department: str
    level: str
    delivery_mode: str
    credits: int
    duration_weeks: int
    rating: float
    tuition_fee_inr: int
    year_offered: int

class CourseCreate(CourseBase):
    pass

class CourseOut(CourseBase):
    course_id: int

    class Config:
        orm_mode = True

