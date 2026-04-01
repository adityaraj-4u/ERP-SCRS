print("======================================")
print(" ERP SYSTEM: STUDENT PROFILE CREATION")
print("======================================")

student_id = input("Enter Student ID: ").strip().upper()
student_name = input("Enter Full Name: ").strip()
program = input("Enter Program (e.g., B.Tech): ").strip()
year = input("Enter Year of Study: ").strip()


print("\n[SUCCESS] Profile Created Successfully!")
print("--- STUDENT PROFILE ---")
print(f"ID      : {student_id}")
print(f"Name    : {student_name}")
print(f"Program : {program}")
print(f"Year    : {year}")
print("-----------------------")