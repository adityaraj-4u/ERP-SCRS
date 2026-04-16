import sys
from services.auth_service import login
from services.course_service import get_all_courses
from services.registration_service import check_prereq, check_seats, check_clash, register, drop_course
from services.advisor_service import view_pending_requests, process_request
from utils.charts import generate_analytics_dashboard
from utils.stats import calculate_department_load
from utils.validators import InputValidator, RegistrationError
from services.registration_service import check_prereq, check_seats, check_clash, register, drop_course, suggest_alternatives
from utils.charts import generate_analytics_dashboard

def main():
    print("==================================================")
    print("🎓 Welcome to the ERP Course Registration System")
    print("==================================================")

    raw_sid = input("Enter Student ID: ")
    try:
        # Use Week 11 Validator to ensure ID isn't blank
        sid = InputValidator.validate_student_id(raw_sid)
    except RegistrationError as e:
        print(f"❌ Validation Error: {e}")
        return

    # Authenticate student
    student = login(sid)

    if not student:
        print("❌ Invalid ID or student not found in database.")
        return

    print(f"\nWelcome {student.name} | Program: {student.program}")
    selected = []

    while True:
        print("\n--- Main Menu ---")
        print("1. View Course Catalog")
        print("2. Register for a Course")
        print("3. Drop a Course")
        print("4. Admin: View Matplotlib Analytics")
        print("5. Advisor: Process Approvals")
        print("6. Admin: View NumPy Stats")
        print("7. Exit")
        
        ch = input("Enter choice (1-7): ")

        if ch == '1':
            courses = get_all_courses()
            print("\n---  Available Courses ---")
            for c in courses:
                print(c) 

        elif ch == '2':
            try:
                raw_code = input("Enter course code (e.g., CS101): ")
                code = InputValidator.validate_course_code(raw_code) 
                
                courses = get_all_courses()
                course = next((c for c in courses if c.code == code), None)

                if not course:
                    print(" Course not found in catalog.")
                    continue
                if not check_prereq(student, course):
                    print(" Prerequisite not satisfied.")
                    continue
                if not check_seats(course):
                    print(" No seats available.")
                    continue
                if check_clash(selected, course):
                    print(f" Time clash detected! {course.code} overlaps with your schedule.")
                    print("\n💡 AI Suggestion Engine: Try these clash-free alternatives instead:")
                    
                    # Fetch suggestions
                    alts = suggest_alternatives(student, selected, courses)
                    
                    if alts:
                        for alt in alts:
                            print(f"   👉 [{alt.code}] {alt.name} | {alt.schedule[0]} at {alt.schedule[1]} ({alt.seats_available()} seats)")
                    else:
                        print("   Sorry, no alternate courses fit your schedule and prerequisites right now.")
                    continue

                register(student, course)
                selected.append(course)
            
            except RegistrationError as e:
                print(f"❌ Validation Error: {e}")

        elif ch == '3':
            try:
                raw_code = input("Enter course code to drop: ")
                code = InputValidator.validate_course_code(raw_code)
                
                course = next((c for c in selected if c.code == code), None)

                if not course:
                    print("❌ You have not registered for this course in this session.")
                    continue

                drop_course(student, course)
                selected.remove(course)
            
            except RegistrationError as e:
                print(f"❌ Validation Error: {e}")

        elif ch == '4':
            print("\n📊 Generating Matplotlib Dashboard...")
            generate_analytics_dashboard()

        elif ch == '5':
            print("\n--- 👨‍🏫 Advisor Approval Panel ---")
            pending = view_pending_requests()
            if not len(pending) == 0:
                try:
                    req_id = int(input("Enter the [Index ID] of the request to process: "))
                    decision = input("Approve or Reject? (A/R): ").strip().upper()
                    if decision == 'A':
                        process_request(req_id, "Approved")
                    elif decision == 'R':
                        process_request(req_id, "Rejected")
                    else:
                        print("❌ Invalid decision. Please enter A or R.")
                except ValueError:
                    print("❌ Invalid ID format. Please enter a number.")

        elif ch == '6':
            calculate_department_load()

        elif ch == '7':
            print("Saving session data... Goodbye!")
            sys.exit()

        else:
            print("❌ Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    main()