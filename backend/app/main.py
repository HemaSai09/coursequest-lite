from fastapi import FastAPI
from .routes import courses, compare, ingest, ask

app = FastAPI(title="CourseQuest Lite API")

# include routers
app.include_router(courses.router, prefix="/api/courses", tags=["courses"])
app.include_router(compare.router, prefix="/api/compare", tags=["compare"])
app.include_router(ingest.router, prefix="/api/ingest", tags=["ingest"])
app.include_router(ask.router, prefix="/api/ask", tags=["ask"])

@app.get("/")
def root():
    return {"message": "CourseQuest Lite API running"}

