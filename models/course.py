class Course:
    def __init__(self, code, name, credits, seats, schedule, prerequisites, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.seats = seats
        self.schedule = schedule  
        self.prerequisites = prerequisites
        self.faculty = faculty    
        self.enrolled = 0   

    def seats_available(self):
        return self.seats - self.enrolled

    def __str__(self):
        
        return f"[{self.code}] {self.name} | Prof: {self.faculty} | Schedule: {self.schedule[0]} at {self.schedule[1]} | ({self.seats_available()} seats left)"
