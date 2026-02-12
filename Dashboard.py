import streamlit as st
import pandas as pd
from database import PlacementDB

# Initialize DB
db = PlacementDB()
db.create_tables()
db.insert_from_csv()
conn = db.conn

st.title("🎓 Placement Eligibility Dashboard")
st.sidebar.header("📋 Eligibility Criteria")

min_problems = st.sidebar.slider("Min Problems Solved", 0, 500, 100)
min_soft_skill = st.sidebar.slider("Min Soft Skill Score", 0, 100, 75)
placement_status = st.sidebar.selectbox(
    "Placement Status", ["All", "Ready", "Placed", "Not Ready"]
)

# Safe Parameterized Query
query = """
SELECT s.student_id, s.name, s.course_batch, s.city, s.graduation_year,
       p.language, p.problems_solved,
       ss.communication, ss.teamwork, ss.presentation,
       pl.placement_status, pl.company_name, pl.placement_package
FROM students s
JOIN programming p ON s.student_id = p.student_id
JOIN soft_skills ss ON s.student_id = ss.student_id
JOIN placements pl ON s.student_id = pl.student_id
WHERE p.problems_solved >= ?
  AND ss.communication >= ?
  AND ss.teamwork >= ?
  AND ss.presentation >= ?
"""

params = [min_problems, min_soft_skill, min_soft_skill, min_soft_skill]

if placement_status != "All":
    query += " AND pl.placement_status = ?"
    params.append(placement_status)

df = pd.read_sql_query(query, conn, params=params)

st.dataframe(df)

st.download_button(
    "📥 Download Results",
    df.to_csv(index=False),
    "filtered_students.csv",
    "text/csv"
)
