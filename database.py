import sqlite3
import pandas as pd

class PlacementDB:
    def __init__(self, db_name="placement.db"):
        self.conn = sqlite3.connect(db_name)
        self.cur = self.conn.cursor()

    def create_tables(self):
        self.cur.executescript("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY,
            name TEXT, age INTEGER, gender TEXT, email TEXT,
            phone TEXT, enrollment_year INTEGER, course_batch TEXT,
            city TEXT, graduation_year INTEGER
        );
        CREATE TABLE IF NOT EXISTS programming (
            programming_id INTEGER PRIMARY KEY,
            student_id INTEGER, language TEXT, problems_solved INTEGER,
            assessments_completed INTEGER, mini_projects INTEGER,
            certifications_earned INTEGER, latest_project_score REAL,
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        );
        CREATE TABLE IF NOT EXISTS soft_skills (
            soft_skill_id INTEGER PRIMARY KEY,
            student_id INTEGER, communication REAL, teamwork REAL,
            presentation REAL, leadership REAL, critical_thinking REAL,
            interpersonal_skills REAL,
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        );
        CREATE TABLE IF NOT EXISTS placements (
            placement_id INTEGER PRIMARY KEY,
            student_id INTEGER, mock_interview_score REAL,
            internships_completed INTEGER, placement_status TEXT,
            company_name TEXT, placement_package REAL,
            interview_rounds_cleared INTEGER, placement_date TEXT,
            FOREIGN KEY(student_id) REFERENCES students(student_id)
        );
        """)
        self.conn.commit()

    def insert_from_csv(self):
        pd.read_csv("students.csv").to_sql("students", self.conn, if_exists="replace", index=False)
        pd.read_csv("programming.csv").to_sql("programming", self.conn, if_exists="replace", index=False)
        pd.read_csv("soft_skills.csv").to_sql("soft_skills", self.conn, if_exists="replace", index=False)
        pd.read_csv("placements.csv").to_sql("placements", self.conn, if_exists="replace", index=False)
