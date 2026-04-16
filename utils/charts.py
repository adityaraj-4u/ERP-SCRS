import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from utils.file_handler import load_csv

def generate_analytics_dashboard():
    """Generates a 5-panel dashboard fulfilling Use Case 5."""
    
    
    df_courses = load_csv("data/courses.csv")
    df_regs = load_csv("data/registrations.csv")

    if df_courses.empty or df_regs.empty:
        print(" Not enough data to generate analytics. Please register some students first.")
        return

    
    enrollment_counts = df_regs['course_code'].value_counts().reset_index()
    enrollment_counts.columns = ['code', 'enrolled']
    
    
    df = pd.merge(df_courses, enrollment_counts, on='code', how='left').fillna(0)
    

    safe_seats = df['seats'].replace(0, 1)
    df['seat_utilization'] = (df['enrolled'] / safe_seats) * 100

   
    df['department'] = df['code'].str.extract(r'([A-Za-z]+)')

    # --- SET UP MATPLOTLIB DASHBOARD ---
    fig = plt.figure(figsize=(15, 10))
    fig.canvas.manager.set_window_title('ERP-SCRS Analytics Dashboard')
    plt.suptitle("🎓 University Enrollment Analytics Dashboard", fontsize=18, fontweight='bold')

    ax1 = plt.subplot(2, 3, 1)
    ax1.bar(df['code'], df['enrolled'], color='#4C72B0')
    ax1.set_title("1. Course Demand", fontsize=12)
    ax1.set_ylabel("Students Enrolled")
    plt.xticks(rotation=45)


    ax2 = plt.subplot(2, 3, 2)
    instructor_data = df.groupby('faculty')['enrolled'].sum().sort_values()
    ax2.barh(instructor_data.index, instructor_data.values, color='#55A868')
    ax2.set_title("2. Instructor Popularity", fontsize=12)
    ax2.set_xlabel("Total Students Taught")

  
    ax3 = plt.subplot(2, 3, 3)
    dept_data = df.groupby('department')['enrolled'].sum()
    if dept_data.sum() > 0:
        ax3.pie(dept_data, labels=dept_data.index, autopct='%1.1f%%', startangle=90, colors=['#C44E52', '#8172B3', '#CCB974'])
    ax3.set_title("3. Department Load (%)", fontsize=12)

   
    ax4 = plt.subplot(2, 3, 4)
    bars = ax4.bar(df['code'], df['seat_utilization'], color='#64B5CD')
    ax4.axhline(100, color='red', linestyle='--', alpha=0.7, label='100% Capacity')
    ax4.set_title("4. Seat Utilization (%)", fontsize=12)
    ax4.set_ylabel("Percentage Filled")
    plt.xticks(rotation=45)
    ax4.legend()

  
    ax5 = plt.subplot(2, 3, 5)
    ax5.hist(df['credits'], bins=np.arange(1, 7)-0.5, color='#EAEAF2', edgecolor='black')
    ax5.set_title("5. Credit Load Chart", fontsize=12)
    ax5.set_xlabel("Credits per Course")
    ax5.set_ylabel("Number of Courses")
    ax5.set_xticks([1, 2, 3, 4, 5, 6])

    
    plt.tight_layout(rect=[0, 0.03, 1, 0.95]) 
    plt.show()
