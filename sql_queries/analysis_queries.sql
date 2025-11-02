-- Student Performance Analysis - SQL Queries
-- Author: Tisha Sharma, LPU
-- Project: Student Performance Analysis

-- ============================================================
-- QUERY 1: Get All Student Records
-- ============================================================
SELECT * FROM students;

-- ============================================================
-- QUERY 2: Find Top 10 Performing Students
-- ============================================================
SELECT 
    Student_ID,
    Name,
    Department,
    Average_Score,
    Attendance_Percent
FROM students
ORDER BY Average_Score DESC
LIMIT 10;

-- ============================================================
-- QUERY 3: Identify At-Risk Students (Below 45% Average)
-- ============================================================
SELECT 
    Student_ID,
    Name,
    Department,
    Average_Score,
    Attendance_Percent,
    Performance_Category
FROM students
WHERE Performance_Category = 'At-Risk'
ORDER BY Average_Score ASC;

-- ============================================================
-- QUERY 4: Department-wise Average Performance
-- ============================================================
SELECT 
    Department,
    COUNT(*) as Total_Students,
    ROUND(AVG(Average_Score), 2) as Avg_Score,
    ROUND(AVG(Attendance_Percent), 2) as Avg_Attendance
FROM students
GROUP BY Department
ORDER BY Avg_Score DESC;

-- ============================================================
-- QUERY 5: Subject-wise Performance Analysis
-- ============================================================
SELECT 
    ROUND(AVG(Mathematics), 2) as Avg_Math,
    ROUND(AVG(Physics), 2) as Avg_Physics,
    ROUND(AVG(Chemistry), 2) as Avg_Chemistry,
    ROUND(AVG(English), 2) as Avg_English,
    ROUND(AVG(Programming), 2) as Avg_Programming
FROM students;

-- ============================================================
-- QUERY 6: Students with Low Attendance (Below 70%)
-- ============================================================
SELECT 
    Student_ID,
    Name,
    Department,
    Attendance_Percent,
    Average_Score
FROM students
WHERE Attendance_Percent < 70
ORDER BY Attendance_Percent ASC;

-- ============================================================
-- QUERY 7: Semester-wise Performance Distribution
-- ============================================================
SELECT 
    Semester,
    COUNT(*) as Total_Students,
    ROUND(AVG(Average_Score), 2) as Avg_Score,
    MIN(Average_Score) as Min_Score,
    MAX(Average_Score) as Max_Score
FROM students
GROUP BY Semester
ORDER BY Semester;

-- ============================================================
-- QUERY 8: Students Failing in Any Subject (Below 35)
-- ============================================================
SELECT 
    Student_ID,
    Name,
    Mathematics,
    Physics,
    Chemistry,
    English,
    Programming
FROM students
WHERE Mathematics < 35 
   OR Physics < 35 
   OR Chemistry < 35 
   OR English < 35 
   OR Programming < 35;

-- ============================================================
-- QUERY 9: Performance Category Distribution
-- ============================================================
SELECT 
    Performance_Category,
    COUNT(*) as Student_Count,
    ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM students), 2) as Percentage
FROM students
GROUP BY Performance_Category
ORDER BY Student_Count DESC;

-- ============================================================
-- QUERY 10: Students Needing Attention (At-Risk + Low Attendance)
-- ============================================================
SELECT 
    Student_ID,
    Name,
    Department,
    Average_Score,
    Attendance_Percent,
    'Low Score & Attendance' as Alert_Reason
FROM students
WHERE Average_Score < 45 AND Attendance_Percent < 70
ORDER BY Average_Score ASC;
