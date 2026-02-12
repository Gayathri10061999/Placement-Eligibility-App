-- 1. Avg programming performance per batch
SELECT course_batch, AVG(problems_solved) AS avg_problems
FROM students s
JOIN programming p ON s.student_id = p.student_id
GROUP BY course_batch;

-- 2. Top 5 ready for placement
SELECT s.name, pl.mock_interview_score
FROM students s
JOIN placements pl ON s.student_id = pl.student_id
WHERE pl.placement_status = 'Ready'
ORDER BY pl.mock_interview_score DESC
LIMIT 5;

-- 3. Soft skills distribution (binning by decile)
SELECT ROUND(communication / 10) * 10 AS bin, COUNT(*) AS count
FROM soft_skills GROUP BY bin;

-- 4. Internship + placement ready
SELECT COUNT(*) FROM placements
WHERE internships_completed > 0 AND placement_status = 'Ready';

-- 5. Branch-wise avg CGPA
SELECT course_batch, AVG(age) AS avg_age
FROM students GROUP BY course_batch;
