from user import User
from course import Course
from registration import Registration

def main():
    # Membuat sistem registrasi
    registration_system = Registration()
    
    # Membuat beberapa kursus
    python_course = Course("Python Programming", "John Doe")
    java_course = Course("Java Programming", "Jane Smith")
    
    # Membuat beberapa user
    user1 = User("alice", "alice@email.com")
    user2 = User("bob", "bob@email.com")
    
    # Mendaftarkan user ke kursus
    registration_system.register(user1, python_course)
    registration_system.register(user2, python_course)
    registration_system.register(user1, java_course)
    
    # Menampilkan informasi
    print("Informasi Kursus:")
    print(python_course.get_info())
    print(java_course.get_info())
    
    print("\nInformasi User:")
    print(user1.get_info())
    print(user2.get_info())

if __name__ == "__main__":
    main() 