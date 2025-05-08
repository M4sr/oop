from .user import User
from .course import Course
from .registration import Registration

def run_kursus():
    try:
        # Buat sistem registrasi
        registration_system = Registration()
        
        # Input kursus
        print("\nMasukkan informasi kursus:")
        print("----------------------------------------")
        nama_kursus = input("Nama Kursus    : ")
        instruktur = input("Instruktur     : ")
        try:
            kapasitas = int(input("Kapasitas      : "))
            kursus = Course(nama_kursus, instruktur, kapasitas)
        except ValueError:
            print("\nKapasitas harus berupa angka!")
            return False
        print("----------------------------------------")
        
        # Input user
        print("\nMasukkan informasi user:")
        print("----------------------------------------")
        username = input("Username       : ")
        email = input("Email          : ")
        user = User(username, email)
        print("----------------------------------------")
        
        # Registrasi
        if registration_system.register(user, kursus):
            print("\n>>> Registrasi Berhasil! <<<")
        else:
            print("\nRegistrasi gagal! Kursus penuh.")
            return False
        
        # Tampilkan informasi kursus
        print("\nRingkasan Kursus:")
        print("----------------------------------------")
        print(f"Nama Kursus    : {kursus.name}")
        print(f"Instruktur     : {kursus.instructor}")
        print(f"Kapasitas      : {len(kursus.students)}/{kursus.capacity}")
        print("----------------------------------------")
        
        # Tampilkan informasi user
        print("\nRingkasan User:")
        print("----------------------------------------")
        print(f"Username       : {user.username}")
        print(f"Email          : {user.email}")
        print(f"Kursus Terdaftar: {len(user.registered_courses)}")
        print("----------------------------------------")
        return True
    except KeyboardInterrupt:
        print("\nOperasi dibatalkan!")
        return False 