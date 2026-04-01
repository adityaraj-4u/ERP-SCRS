class Course:
    def __init__(self, code, title, max_seats):
        self.code = code
        self.title = title
        self.max_seats = max_seats
        self.filled_seats = 0

    def is_full(self):
        return self.filled_seats >= self.max_seats

class Student:
    def __init__(self, s_id, name):
        self.s_id = s_id
        self.name = name
        self.registered = []

    def register(self, course_obj):
        if course_obj.is_full():
            print(f"[ERROR] {course_obj.code} is full.")
        else:
            course_obj.filled_seats += 1
            self.registered.append(course_obj.code)
            print(f"[SUCCESS] {self.name} registered for {course_obj.title}")

c1 = Course("CS101", "Python", 2)
s1 = Student("S1", "Alice")

s1.register(c1)
print(f"[INFO] Seats filled in {c1.code}: {c1.filled_seats}/{c1.max_seats}")