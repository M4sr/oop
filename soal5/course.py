class Course:
    def __init__(self, name, instructor, capacity=30):
        self.name = name
        self.instructor = instructor
        self.capacity = capacity
        self.students = []
    
    def add_student(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            return True
        return False
    
    def get_info(self):
        return f"Kursus: {self.name}, Instruktur: {self.instructor}, Kapasitas: {len(self.students)}/{self.capacity}" 