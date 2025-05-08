class Registration:
    def __init__(self):
        self.registrations = {}
    
    def register(self, user, course):
        if course.add_student(user):
            user.register_course(course)
            if course.name not in self.registrations:
                self.registrations[course.name] = []
            self.registrations[course.name].append(user)
            return True
        return False
    
    def get_course_registrations(self, course_name):
        return self.registrations.get(course_name, []) 