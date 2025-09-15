CREATE TABLE courses (
    course_id SERIAL PRIMARY KEY,
    course_name TEXT NOT NULL,
    department TEXT NOT NULL,
    level VARCHAR(10) CHECK (level IN ('UG','PG')),
    delivery_mode VARCHAR(10) CHECK (delivery_mode IN ('online','offline','hybrid')),
    credits INT,
    duration_weeks INT,
    rating FLOAT,
    tuition_fee_inr INT,
    year_offered INT
);

-- indexes
CREATE INDEX idx_department ON courses(department);
CREATE INDEX idx_level ON courses(level);
CREATE INDEX idx_fee ON courses(tuition_fee_inr);
CREATE INDEX idx_name ON courses(course_name);

