# models/registration.py

class Registration:
    def __init__(self, student_id, course_code, status="Pending"):
        self.student_id = student_id
        self.course_code = course_code
        self.status = status  

    def __str__(self):
        return f"Student: {self.student_id} | Course: {self.course_code} | Status: {self.status}"
