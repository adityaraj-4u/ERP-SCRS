academic_timetable = {
    "MON": {}, "TUE": {}, "WED": {}, "THU": {}, "FRI": {}
}

def schedule_course(day, time_slot, course_code, faculty_name):
    """Assigns a course to a slot and detects conflicts."""
    day = day.strip().upper()
    time_slot = time_slot.strip()
    
    if day not in academic_timetable:
        print(f"[ERROR] Invalid day '{day}'.")
        return False

    # Conflict Detection
    if time_slot in academic_timetable[day]:
        existing_class = academic_timetable[day][time_slot]
        print(f"[ERROR] Conflict! {day} at {time_slot} is booked for {existing_class['course']}.")
        return False

    academic_timetable[day][time_slot] = {
        "course": course_code.upper(),
        "faculty": faculty_name
    }
    print(f"[SUCCESS] Scheduled {course_code} on {day} at {time_slot}.")
    return True

def view_timetable():
    print("\n==================================")
    print("    WEEKLY ACADEMIC TIMETABLE")
    print("==================================")
    for day, slots in academic_timetable.items():
        print(f"\n[{day}]")
        if not slots:
            print("  No classes scheduled.")
        else:
            for time_slot in sorted(slots.keys()):
                details = slots[time_slot]
                print(f"  {time_slot} | {details['course']:<8} | Faculty: {details['faculty']}")

if __name__ == "__main__":
    print("[INFO] Testing Timetable Module...")
    schedule_course("MON", "09:00", "CS101", "Dr. Smith")
    schedule_course("MON", "11:00", "MA101", "Prof. Johnson")
    
    # Trigger a conflict
    schedule_course("MON", "09:00", "PH101", "Dr. Banner")
    
    view_timetable()