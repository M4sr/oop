class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.registered_courses = []
    
    def register_course(self, course):
        self.registered_courses.append(course)
    
    def get_info(self):
        return f"Username: {self.username}, Email: {self.email}, Kursus terdaftar: {len(self.registered_courses)}" 