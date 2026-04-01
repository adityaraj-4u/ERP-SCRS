catalog = [
    ["CS101", "Python Programming", 4, 50],
    ["MA101", "Calculus I", 3, 60]
]
my_schedule = []

def display_catalog():
    print("\n--- CATALOG ---")
    for c in catalog:
        print(f"{c[0]}: {c[1]}")

def register_course(course_code):
    if course_code in my_schedule:
        print("[ERROR] Already registered for this course.")
        return
        
    for c in catalog:
        if c[0] == course_code:
            my_schedule.append(course_code)
            print(f"[SUCCESS] Registered for {c[1]}")
            return
            
    print("[ERROR] Course Code not found.")

def main():
    while True:
        print("\n1. Catalog | 2. Register | 3. Exit")
        ch = input("Select: ").strip()
        if ch == '1':
            display_catalog()
        elif ch == '2':
            code = input("Course Code: ").strip().upper()
            register_course(code)
        elif ch == '3':
            break

if __name__ == "__main__":
    main()