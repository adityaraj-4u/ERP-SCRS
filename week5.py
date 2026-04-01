courses_db = {
    "CS101": {
        "title": "Python", 
        "schedule": ("MON", "10:00"),
        "prereqs": set()              
    },
    "CS102": {
        "title": "Data Structures", 
        "schedule": ("TUE", "11:00"), 
        "prereqs": {"CS101"}        
    }
}

student_completed = {"CS101"}
student_registered = []

print("\n--- ATTEMPTING REGISTRATION ---")
target = "CS102"
course = courses_db[target]

if course["prereqs"].issubset(student_completed):
    student_registered.append(target)
    print(f"[SUCCESS] Registered for {course['title']}")
else:
    missing = course["prereqs"] - student_completed
    print(f"[ERROR] Missing prerequisites: {missing}")