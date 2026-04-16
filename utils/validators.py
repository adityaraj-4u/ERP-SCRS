# utils/validators.py

class RegistrationError(Exception):
    """Custom exception for registration logic failures."""
    pass

class InputValidator:
    @staticmethod
    def validate_course_code(code):
        """Ensures the course code follows a standard format (e.g., CS101)"""
        if not code or len(code) < 4:
            raise RegistrationError("Invalid Course Code format. Must be at least 4 characters.")
        return code.strip().upper()

    @staticmethod
    def validate_student_id(sid):
        """Ensures student ID is not empty"""
        if not sid:
            raise RegistrationError("Student ID cannot be empty.")
        return str(sid).strip()