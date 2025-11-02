# Quick Start Guide

## Student Performance Analysis Project

### What's in This Project?

📊 **100 student records** with grades, attendance, and performance data  
💻 **Python scripts** for statistical analysis using NumPy  
🗃️ **SQL queries** for database analysis (10 ready-to-use queries)  
📈 **Excel guide** for creating pivot tables and dashboards  
📸 **4 visualizations** showing key insights  

---

## How to Get Started

### Option 1: Python Analysis (Recommended)

**Step 1: Install Python**
- Download Python from python.org (version 3.8+)
- Check installation: `python --version`

**Step 2: Install Packages**
```bash
pip install pandas numpy matplotlib seaborn
```

**Step 3: Run Analysis**
```bash
cd code
python numpy_analysis.py
python visualizations.py
```

**Results**: Check `output` folder for reports, `images` folder for charts

---

### Option 2: SQL Analysis

**Step 1: Import Data**
- Use any SQL database (MySQL, PostgreSQL, SQLite)
- Import `data/student_records.csv` as a table named "students"

**Step 2: Run Queries**
- Open `sql_queries/analysis_queries.sql`
- Run queries one by one to get insights
- 10 pre-written queries included!

**Example Query**:
```sql
-- Find at-risk students
SELECT Student_ID, Name, Average_Score, Attendance_Percent
FROM students
WHERE Average_Score < 45
ORDER BY Average_Score;
```

---

### Option 3: Excel Pivot Tables

**Step 1: Open in Excel**
- Open `data/student_records.csv` in Microsoft Excel

**Step 2: Create Pivot Table**
- Select all data (Ctrl+A)
- Insert → PivotTable
- Follow `EXCEL_PIVOT_GUIDE.md` for detailed instructions

**Step 3: Create Dashboard**
- Make 5 pivot tables as described in the guide
- Add charts and formatting
- Create an interactive dashboard

---

## Understanding the Data

### File: student_records.csv

**Columns**:
- `Student_ID`: Unique identifier (STU0001, STU0002, etc.)
- `Name`: Student name
- `Department`: CS, Electronics, Mechanical, or Civil
- `Semester`: 1-6
- `Mathematics`: Score out of 100
- `Physics`: Score out of 100
- `Chemistry`: Score out of 100
- `English`: Score out of 100
- `Programming`: Score out of 100
- `Attendance_Percent`: Attendance percentage
- `Total_Score`: Sum of all subject scores
- `Average_Score`: Average of all subjects
- `Performance_Category`: Excellent/Good/Average/At-Risk

---

## What You'll Learn

### 1. SQL Skills
✓ SELECT statements with WHERE clauses
✓ GROUP BY and aggregation functions
✓ Sorting with ORDER BY
✓ Filtering with comparison operators

### 2. NumPy Skills
✓ Array operations
✓ Statistical functions (mean, median, std)
✓ Correlation analysis
✓ Data manipulation

### 3. Excel Skills
✓ Creating pivot tables
✓ Data aggregation and summarization
✓ Conditional formatting
✓ Creating dashboards

### 4. Data Analysis Skills
✓ Identifying patterns and trends
✓ Finding at-risk populations
✓ Correlation analysis
✓ Report generation

---

## Key Questions This Analysis Answers

1. **Who are the at-risk students?**
   - Run SQL query #3 or check `at_risk_students.csv`

2. **Which subject is hardest?**
   - Run Python analysis or SQL query #5

3. **Does attendance matter?**
   - Check visualization #3 (strong correlation!)

4. **Which department performs best?**
   - Run SQL query #4 or check visualization #4

5. **How many students are failing?**
   - Check performance distribution chart

---

## Uploading to GitHub

1. **Create Repository**
   - Go to github.com/new
   - Name: `Student-Performance-Analysis`
   - Public repository
   - Create

2. **Upload Files**
   - Drag and drop all folders
   - Or use Git commands:
   ```bash
   git init
   git add .
   git commit -m "Student Performance Analysis project"
   git remote add origin YOUR_REPO_URL
   git push -u origin main
   ```

3. **Update README**
   - Replace email and contact info with yours
   - Add your name to the author section

---

## Common Questions

**Q: Do I need to know SQL to use this?**  
A: No! You can use just Python or Excel. SQL is optional.

**Q: Can I modify the data?**  
A: Yes! Add more students, subjects, or parameters as needed.

**Q: How long does analysis take?**  
A: Python scripts run in under 1 minute.

**Q: Can I use this for my college project?**  
A: Absolutely! It's designed for educational purposes.

---

## Troubleshooting

**Issue**: "Module not found" error  
**Solution**: Run `pip install -r requirements.txt`

**Issue**: CSV file not found  
**Solution**: Make sure you're in the correct directory

**Issue**: Excel won't open CSV  
**Solution**: Right-click → Open With → Excel

---

## Next Steps

1. ✓ Extract the ZIP file
2. □ Read this guide
3. □ Choose your method (Python/SQL/Excel)
4. □ Run the analysis
5. □ Review the outputs
6. □ Upload to GitHub
7. □ Add to your portfolio!

---

**Created by Tisha Sharma | LPU**  
**Good luck with your analysis!** 🚀
