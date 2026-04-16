# utils/stats.py
import pandas as pd
import numpy as np
from utils.file_handler import load_csv

def calculate_department_load():
    """Uses NumPy to calculate the average seats filled across all courses."""
    df_courses = load_csv("data/courses.csv")
    df_regs = load_csv("data/registrations.csv")
    
    if df_courses.empty or df_regs.empty:
        print("Not enough data to calculate stats.")
        return

    
    enrollment_counts = df_regs['course_code'].value_counts().values
    
    if len(enrollment_counts) > 0:
        
        avg_enrollment = np.mean(enrollment_counts)
        max_enrollment = np.max(enrollment_counts)
        
        print("\n--- NumPy Analytics Report ---")
        print(f"Average students per active course: {avg_enrollment:.1f}")
        print(f"Highest enrollment count in a single course: {max_enrollment}")
    else:
        print("No active enrollments to analyze.")
