catalog = [
    ["CS101", "Python Programming", 4, 50],
    ["CS102", "Data Structures", 4, 40],
    ["MA101", "Calculus I", 3, 60]
]

registered_courses = []

while True:
    print("\n1. View All Courses | 2. Search Course | 3. Register | 4. Exit")
    choice = input("Select: ").strip()
    
    if choice == '1':
        print("\n--- COURSE CATALOG ---")
        for course in catalog:
            print(f"{course[0]}: {course[1]} ({course[2]} Credits) - Seats: {course[3]}")
            
    elif choice == '2':
        query = input("Enter keyword to search: ").strip().lower()
        print("\n--- SEARCH RESULTS ---")
        found = False
        for course in catalog:
            if query in course[1].lower() or query in course[0].lower():
                print(f"{course[0]} - {course[1]}")
                found = True
        if not found:
            print("[INFO] No courses found matching your query.")
            
    elif choice == '3':
        code = input("Enter Course Code: ").strip().upper()
        registered_courses.append(code)
        print(f"[SUCCESS] Added {code} to your schedule. Current schedule: {registered_courses}")
        
    elif choice == '4':
        break