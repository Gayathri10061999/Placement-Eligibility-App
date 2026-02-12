import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect("placement.db")

st.title("🎓 Placement Eligibility Dashboard")
st.sidebar.header("📋 Eligibility Criteria")

min_problems = st.sidebar.slider("Min Problems Solved", 0, 500, 100)
min_soft_skill = st.sidebar.slider("Min Soft Skill Score", 0, 100, 75)
placement_status = st.sidebar.selectbox("Placement Status", ["All", "Ready", "Placed", "Not Ready"])

query = f"""
SELECT s.student_id, s.name, s.course_batch, s.city, s.graduation_year,
       p.language, p.problems_solved, ss.communication, ss.teamwork, ss.presentation,
       pl.placement_status, pl.company_name, pl.placement_package
FROM students s
JOIN programming p ON s.student_id = p.student_id
JOIN soft_skills ss ON s.student_id = ss.student_id
JOIN placements pl ON s.student_id = pl.student_id
WHERE p.problems_solved >= {min_problems}
  AND ss.communication >= {min_soft_skill}
  AND ss.teamwork >= {min_soft_skill}
  AND ss.presentation >= {min_soft_skill}
"""

if placement_status != "All":
    query += f" AND pl.placement_status = '{placement_status}'"

df = pd.read_sql_query(query, conn)
st.dataframe(df)

st.download_button("📥 Download Results", df.to_csv(index=False), "filtered_students.csv", "text/csv")
