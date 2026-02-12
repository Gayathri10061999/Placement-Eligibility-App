from faker import Faker
import pandas as pd
import random
from datetime import datetime
fake = Faker()

NUM_STUDENTS = 100
students, programming, soft_skills, placements = [], [], [], []

for i in range(1, NUM_STUDENTS + 1):
    # Students Table
    name = fake.name()
    gender = random.choice(["Male", "Female", "Other"])
    email = fake.email()
    phone = fake.phone_number()
    enrollment_year = random.choice([2020, 2021, 2022])
    course_batch = f"DS-{enrollment_year}"
    city = fake.city()
    graduation_year = enrollment_year + 4
    age = random.randint(18, 24)
    student = [i, name, age, gender, email, phone, enrollment_year, course_batch, city, graduation_year]
    students.append(student)

    # Programming Table
    programming.append([
        i, i, random.choice(["Python", "SQL", "Java"]),
        random.randint(10, 500),
        random.randint(1, 10),
        random.randint(1, 5),
        random.randint(0, 3),
        round(random.uniform(60, 100), 2)
    ])

    # Soft Skills Table
    soft_skills.append([
        i, i,
        round(random.uniform(60, 100), 2),  # Communication
        round(random.uniform(60, 100), 2),
        round(random.uniform(60, 100), 2),
        round(random.uniform(60, 100), 2),
        round(random.uniform(60, 100), 2),
        round(random.uniform(60, 100), 2),
    ])

    # Placements Table
    placed = random.choice(["Ready", "Not Ready", "Placed"])
    company = fake.company() if placed == "Placed" else None
    package = round(random.uniform(4, 15), 2) if placed == "Placed" else None
    placements.append([
        i, i,
        round(random.uniform(50, 100), 2),
        random.randint(0, 3),
        placed,
        company,
        package,
        random.randint(0, 5),
        fake.date_this_decade() if placed == "Placed" else None
    ])

# Convert to DataFrames
df_students = pd.DataFrame(students, columns=[
    "student_id", "name", "age", "gender", "email", "phone",
    "enrollment_year", "course_batch", "city", "graduation_year"
])
df_programming = pd.DataFrame(programming, columns=[
    "programming_id", "student_id", "language", "problems_solved",
    "assessments_completed", "mini_projects", "certifications_earned", "latest_project_score"
])
df_soft_skills = pd.DataFrame(soft_skills, columns=[
    "soft_skill_id", "student_id", "communication", "teamwork",
    "presentation", "leadership", "critical_thinking", "interpersonal_skills"
])
df_placements = pd.DataFrame(placements, columns=[
    "placement_id", "student_id", "mock_interview_score", "internships_completed",
    "placement_status", "company_name", "placement_package",
    "interview_rounds_cleared", "placement_date"
])

# Save to CSV (optional)
df_students.to_csv("students.csv", index=False)
df_programming.to_csv("programming.csv", index=False)
df_soft_skills.to_csv("soft_skills.csv", index=False)
df_placements.to_csv("placements.csv", index=False)
