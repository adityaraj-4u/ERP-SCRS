import pandas as pd
from utils.file_handler import load_csv, save_csv

def check_prereq(student, course):
    
    raw_reqs = [str(p).strip().upper() for p in course.prerequisites]
    raw_completed = [str(c).strip().upper() for c in student.completed]

    
    actual_reqs = [p for p in raw_reqs if p != "" and p not in ["NONE", "NAN", "NULL"]]

    
    if len(actual_reqs) == 0:
        return True

    
    for req in actual_reqs:
        if req not in raw_completed:
            
            print(f"System Blocked: Course needs '{req}', but your profile shows {raw_completed}")
            return False

    return True
def check_seats(course):
    return course.seats_available() > 0

def check_clash(selected_courses, new_course):
    for c in selected_courses:
        if c.schedule == new_course.schedule:
            return True
    return False

def register(student, course):
    df = load_csv("data/registrations.csv")

    new_row = {
        "student_id": student.id, 
        "course_code": course.code
    }

    
    if df.empty:
        df = pd.DataFrame([new_row])
    else:
        df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
        
    save_csv(df, "data/registrations.csv")
    course.enrolled += 1
    print(f" Registered successfully for {course.code}!")

def drop_course(student, course):
    
    df = load_csv("data/registrations.csv")
    
    if not df.empty:
        
        df = df[~((df["student_id"] == student.id) & (df["course_code"] == course.code))]
        save_csv(df, "data/registrations.csv")
        course.enrolled -= 1
        print(f"{course.code} dropped successfully.")
def suggest_alternatives(student, selected_courses, all_courses):
    """Finds up to 3 courses the student can take that do NOT clash."""
    suggestions = []
    
    for c in all_courses:
        
        if any(selected.code == c.code for selected in selected_courses):
            continue
            
        
        if check_prereq(student, c) and check_seats(c) and not check_clash(selected_courses, c):
            suggestions.append(c)
            
        if len(suggestions) >= 3:
            break
            
    return suggestions
