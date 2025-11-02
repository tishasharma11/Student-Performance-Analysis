# Student Performance Analysis - NumPy Statistics
# Author: Tisha Sharma, LPU
# Uses NumPy for statistical analysis

import pandas as pd
import numpy as np

print("="*70)
print("STUDENT PERFORMANCE ANALYSIS - NumPy Statistics")
print("="*70)

# Load data
df = pd.read_csv('../data/student_records.csv')
print(f"\n✓ Loaded {len(df)} student records\n")

# ============================================================
# 1. BASIC STATISTICS USING NUMPY
# ============================================================
print("="*70)
print("1. BASIC STATISTICS (NumPy)")
print("="*70)

subjects = ['Mathematics', 'Physics', 'Chemistry', 'English', 'Programming']

for subject in subjects:
    scores = df[subject].values  # Convert to NumPy array
    print(f"\n{subject}:")
    print(f"  Mean:       {np.mean(scores):.2f}")
    print(f"  Median:     {np.median(scores):.2f}")
    print(f"  Std Dev:    {np.std(scores):.2f}")
    print(f"  Min:        {np.min(scores):.2f}")
    print(f"  Max:        {np.max(scores):.2f}")

# ============================================================
# 2. PERFORMANCE TRENDS ANALYSIS
# ============================================================
print("\n" + "="*70)
print("2. PERFORMANCE TRENDS")
print("="*70)

# Overall class performance
overall_avg = np.mean(df['Average_Score'].values)
overall_median = np.median(df['Average_Score'].values)
overall_std = np.std(df['Average_Score'].values)

print(f"\nOverall Class Performance:")
print(f"  Average Score:  {overall_avg:.2f}")
print(f"  Median Score:   {overall_median:.2f}")
print(f"  Std Deviation:  {overall_std:.2f}")

# Attendance correlation
attendance = df['Attendance_Percent'].values
avg_scores = df['Average_Score'].values
correlation = np.corrcoef(attendance, avg_scores)[0, 1]

print(f"\nAttendance-Performance Correlation: {correlation:.3f}")
if correlation > 0.5:
    print("  → Strong positive correlation (Good attendance = Better scores)")
elif correlation > 0.3:
    print("  → Moderate positive correlation")
else:
    print("  → Weak correlation")

# ============================================================
# 3. AT-RISK STUDENT IDENTIFICATION
# ============================================================
print("\n" + "="*70)
print("3. AT-RISK STUDENTS")
print("="*70)

# Students with average < 45
at_risk_mask = df['Average_Score'] < 45
at_risk_students = df[at_risk_mask]

print(f"\nTotal At-Risk Students: {len(at_risk_students)}")
print(f"Percentage: {(len(at_risk_students)/len(df)*100):.1f}%")

if len(at_risk_students) > 0:
    print("\nAt-Risk Students Details:")
    for idx, row in at_risk_students.iterrows():
        print(f"  {row['Student_ID']} - {row['Name']}: Avg {row['Average_Score']:.2f}, "
              f"Attendance {row['Attendance_Percent']}%")

# Students with low attendance
low_attendance = df[df['Attendance_Percent'] < 70]
print(f"\nStudents with Low Attendance (<70%): {len(low_attendance)}")

# ============================================================
# 4. DEPARTMENT-WISE ANALYSIS
# ============================================================
print("\n" + "="*70)
print("4. DEPARTMENT-WISE PERFORMANCE")
print("="*70)

for dept in df['Department'].unique():
    dept_data = df[df['Department'] == dept]['Average_Score'].values
    print(f"\n{dept}:")
    print(f"  Students:   {len(dept_data)}")
    print(f"  Avg Score:  {np.mean(dept_data):.2f}")
    print(f"  Best:       {np.max(dept_data):.2f}")
    print(f"  Worst:      {np.min(dept_data):.2f}")

# ============================================================
# 5. SUBJECT-WISE DIFFICULTY ANALYSIS
# ============================================================
print("\n" + "="*70)
print("5. SUBJECT DIFFICULTY RANKING")
print("="*70)

subject_means = {subject: np.mean(df[subject].values) for subject in subjects}
sorted_subjects = sorted(subject_means.items(), key=lambda x: x[1])

print("\nSubjects ranked by difficulty (lowest avg = hardest):")
for i, (subject, avg) in enumerate(sorted_subjects, 1):
    print(f"  {i}. {subject}: {avg:.2f}")

# ============================================================
# 6. GENERATE SUMMARY REPORT
# ============================================================
print("\n" + "="*70)
print("6. GENERATING SUMMARY REPORTS")
print("="*70)

# Create at-risk report
at_risk_report = df[df['Performance_Category'] == 'At-Risk'][
    ['Student_ID', 'Name', 'Department', 'Average_Score', 'Attendance_Percent']
].sort_values('Average_Score')

at_risk_report.to_csv('../output/at_risk_students.csv', index=False)
print(f"\n✓ At-risk students report saved: {len(at_risk_report)} students")

# Create department summary
dept_summary = df.groupby('Department').agg({
    'Average_Score': ['mean', 'min', 'max', 'count'],
    'Attendance_Percent': 'mean'
}).round(2)

dept_summary.to_csv('../output/department_summary.csv')
print("✓ Department summary saved")

# Create subject-wise summary
subject_summary = pd.DataFrame({
    'Subject': subjects,
    'Average': [np.mean(df[s].values) for s in subjects],
    'Median': [np.median(df[s].values) for s in subjects],
    'Std_Dev': [np.std(df[s].values) for s in subjects],
    'Pass_Rate': [(df[s] >= 35).sum() / len(df) * 100 for s in subjects]
}).round(2)

subject_summary.to_csv('../output/subject_summary.csv', index=False)
print("✓ Subject-wise summary saved")

print("\n" + "="*70)
print("✓ ANALYSIS COMPLETE - Check output folder for reports")
print("="*70)
