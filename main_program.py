import os
import sys
import time
from soal1.interface import run_matematika
from soal2.interface import run_mahasiswa
from soal3.interface import run_hewan
from soal4.interface import run_perpustakaan
from soal5.interface import run_kursus

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def exit_program():
    clear_screen()
    print("\nTerima kasih telah menggunakan program ini!")
    print("Program akan keluar dalam 3 detik...")
    import time
    time.sleep(3)
    sys.exit(0)

def handle_exit():
    try:
        exit_program()
    except KeyboardInterrupt:
        sys.exit(0)

def menu_utama():
    try:
        while True:
            clear_screen()
            print("=== PROGRAM OOP MODULAR ===")
            print("1. Modul Matematika")
            print("2. Package Mahasiswa")
            print("3. Class Hewan")
            print("4. Package Perpustakaan")
            print("5. Sistem Pendaftaran Kursus")
            print("0. Keluar")
            print("\nTekan Ctrl+C untuk keluar dari program")
            
            try:
                pilihan = input("\nPilih menu (0-5): ")
                
                if pilihan == "1":
                    clear_screen()
                    print("=== MODUL MATEMATIKA ===")
                    print("Tekan Ctrl+C untuk kembali ke menu utama")
                    run_matematika()
                elif pilihan == "2":
                    clear_screen()
                    print("=== PACKAGE MAHASISWA ===")
                    print("Tekan Ctrl+C untuk kembali ke menu utama")
                    run_mahasiswa()
                elif pilihan == "3":
                    clear_screen()
                    print("=== CLASS HEWAN ===")
                    print("Tekan Ctrl+C untuk kembali ke menu utama")
                    run_hewan()
                elif pilihan == "4":
                    clear_screen()
                    print("=== PACKAGE PERPUSTAKAAN ===")
                    print("Tekan Ctrl+C untuk kembali ke menu utama")
                    run_perpustakaan()
                elif pilihan == "5":
                    clear_screen()
                    print("=== SISTEM PENDAFTARAN KURSUS ===")
                    print("Tekan Ctrl+C untuk kembali ke menu utama")
                    run_kursus()
                elif pilihan == "0":
                    handle_exit()
                else:
                    print("\nPilihan tidak valid!")
                
                if pilihan != "0":
                    input("\nTekan Enter untuk kembali ke menu utama...")
            
            except KeyboardInterrupt:
                print("\nKembali ke menu utama...")
                time.sleep(1)
                continue
                
    except KeyboardInterrupt:
        handle_exit()

if __name__ == "__main__":
    menu_utama() 