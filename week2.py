print("======================================")
print("       ERP REGISTRATION SYSTEM")
print("======================================")


student_id = input("Enter Student ID to login: ").strip().upper()
print(f"\n[INFO] Welcome, {student_id}!")

while True:
    print("\n--- MAIN DASHBOARD ---")
    print("1. View Courses")
    print("2. Register for a Course")
    print("3. Exit System")
    
    choice = input("Select an option (1-3): ").strip()
    
    if choice == '1':
        print("\n[INFO] Viewing Courses... (Catalog empty in Week 2)")
    elif choice == '2':
        course_code = input("Enter Course Code to Register: ").strip().upper()
        print(f"[SUCCESS] Registration request for {course_code} submitted.")
    elif choice == '3':
        print("[INFO] Exiting System. Goodbye!")
        break
    else:
        print("[ERROR] Invalid selection. Please choose 1, 2, or 3.")