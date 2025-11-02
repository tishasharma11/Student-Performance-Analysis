# Student Performance Visualizations
# Author: Tisha Sharma, LPU

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

print("="*70)
print("GENERATING VISUALIZATIONS")
print("="*70)

# Set style
sns.set_style("whitegrid")

# Load data
df = pd.read_csv('../data/student_records.csv')
print(f"\n✓ Data loaded: {len(df)} records\n")

# ============================================================
# VISUALIZATION 1: Performance Distribution
# ============================================================
print("[1/4] Creating performance distribution chart...")

plt.figure(figsize=(10, 6))
performance_counts = df['Performance_Category'].value_counts()
colors = {'Excellent': '#2ecc71', 'Good': '#3498db', 'Average': '#f39c12', 'At-Risk': '#e74c3c'}
bars = plt.bar(performance_counts.index, performance_counts.values, 
               color=[colors.get(x, 'gray') for x in performance_counts.index], alpha=0.8)

plt.xlabel('Performance Category', fontsize=12, fontweight='bold')
plt.ylabel('Number of Students', fontsize=12, fontweight='bold')
plt.title('Student Performance Distribution\nNov-Dec 2024', fontsize=14, fontweight='bold')
plt.grid(axis='y', alpha=0.3)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height,
             f'{int(height)}',
             ha='center', va='bottom', fontweight='bold')

plt.tight_layout()
plt.savefig('../images/01_performance_distribution.png', dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Saved: 01_performance_distribution.png")

# ============================================================
# VISUALIZATION 2: Subject-wise Average Scores
# ============================================================
print("[2/4] Creating subject-wise performance chart...")

subjects = ['Mathematics', 'Physics', 'Chemistry', 'English', 'Programming']
subject_avgs = [df[subject].mean() for subject in subjects]

plt.figure(figsize=(10, 6))
colors_list = ['#e74c3c', '#3498db', '#2ecc71', '#f39c12', '#9b59b6']
bars = plt.barh(subjects, subject_avgs, color=colors_list, alpha=0.8)

plt.xlabel('Average Score', fontsize=12, fontweight='bold')
plt.ylabel('Subject', fontsize=12, fontweight='bold')
plt.title('Subject-wise Average Performance\nNov-Dec 2024', fontsize=14, fontweight='bold')
plt.xlim(0, 100)
plt.axvline(x=60, color='red', linestyle='--', alpha=0.5, label='Pass Threshold')
plt.legend()
plt.grid(axis='x', alpha=0.3)

# Add value labels
for i, (bar, val) in enumerate(zip(bars, subject_avgs)):
    plt.text(val + 1, i, f'{val:.1f}', va='center', fontweight='bold')

plt.tight_layout()
plt.savefig('../images/02_subject_performance.png', dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Saved: 02_subject_performance.png")

# ============================================================
# VISUALIZATION 3: Attendance vs Performance
# ============================================================
print("[3/4] Creating attendance vs performance scatter plot...")

plt.figure(figsize=(10, 6))
colors_map = {'Excellent': '#2ecc71', 'Good': '#3498db', 
              'Average': '#f39c12', 'At-Risk': '#e74c3c'}

for category in df['Performance_Category'].unique():
    cat_data = df[df['Performance_Category'] == category]
    plt.scatter(cat_data['Attendance_Percent'], cat_data['Average_Score'],
                label=category, alpha=0.6, s=80, color=colors_map[category])

plt.xlabel('Attendance Percentage', fontsize=12, fontweight='bold')
plt.ylabel('Average Score', fontsize=12, fontweight='bold')
plt.title('Attendance vs Academic Performance\nNov-Dec 2024', fontsize=14, fontweight='bold')
plt.legend(title='Performance Category', frameon=True, shadow=True)
plt.grid(True, alpha=0.3)

# Add trend line
z = np.polyfit(df['Attendance_Percent'], df['Average_Score'], 1)
p = np.poly1d(z)
plt.plot(df['Attendance_Percent'].sort_values(), 
         p(df['Attendance_Percent'].sort_values()),
         "r--", alpha=0.5, linewidth=2, label='Trend')

plt.tight_layout()
plt.savefig('../images/03_attendance_vs_performance.png', dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Saved: 03_attendance_vs_performance.png")

# ============================================================
# VISUALIZATION 4: Department-wise Performance
# ============================================================
print("[4/4] Creating department-wise comparison...")

plt.figure(figsize=(10, 6))
dept_data = df.groupby('Department')['Average_Score'].mean().sort_values()

bars = plt.barh(dept_data.index, dept_data.values, 
                color='steelblue', alpha=0.8)

plt.xlabel('Average Score', fontsize=12, fontweight='bold')
plt.ylabel('Department', fontsize=12, fontweight='bold')
plt.title('Department-wise Average Performance\nNov-Dec 2024', fontsize=14, fontweight='bold')
plt.xlim(0, 100)
plt.grid(axis='x', alpha=0.3)

# Add value labels
for i, (dept, val) in enumerate(dept_data.items()):
    plt.text(val + 1, i, f'{val:.1f}', va='center', fontweight='bold')

plt.tight_layout()
plt.savefig('../images/04_department_performance.png', dpi=300, bbox_inches='tight')
plt.close()
print("   ✓ Saved: 04_department_performance.png")

print("\n" + "="*70)
print("✓ All visualizations created successfully!")
print("="*70)
