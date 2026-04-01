from datetime import datetime

class Record:
    """Base class providing audit functionality"""
    def __init__(self):
        self._last_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def update_timestamp(self):
        self._last_modified = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def get_timestamp(self):
        return self._last_modified

class Course(Record):
    def __init__(self, code, title):
        super().__init__()
        self.code = code
        self.title = title

class Student(Record):
    def __init__(self, s_id, name):
        super().__init__()
        self.s_id = s_id
        self.name = name

s1 = Student("S101", "Alice")
print(f"[INFO] Student Record Created At: {s1.get_timestamp()}")

s1.name = "Alice Smith"
s1.update_timestamp()
print(f"[INFO] Student Record Updated At: {s1.get_timestamp()}")