from utils.file_handler import load_csv
from models.course import Course
import pandas as pd

def get_all_courses():
    df_courses = load_csv("data/courses.csv")
    df_regs = load_csv("data/registrations.csv")
    
    # SAFETY: If the file is missing or empty, return an empty list instead of None
    if df_courses is None or df_courses.empty:
        return []
        
    courses = []

    for _, row in df_courses.iterrows():
        try:
            # Clean prerequisites
            raw_prereq = str(row.get('prereqs', 'None')).strip().lower()
            if raw_prereq in ["none", "nan", "", "null"]:
                prereqs = []
            else:
                prereqs = [p.strip().upper() for p in raw_prereq.split('|')]

            schedule = (str(row.get('day', 'TBD')), str(row.get('time', 'TBD')))

            course = Course(
                str(row['code']),
                str(row['name']),
                int(row['credits']),
                int(row['seats']),
                schedule,
                prereqs,
                str(row.get('faculty', 'Staff')) 
            )

            # Count enrollments from registrations file
            if df_regs is not None and not df_regs.empty:
                course.enrolled = len(df_regs[df_regs["course_code"] == course.code])

            courses.append(course)
        except Exception as e:
            print(f"⚠️ Skipping a row in courses.csv due to error: {e}")
            continue

    return courses