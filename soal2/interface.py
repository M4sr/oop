from .mahasiswa import Mahasiswa, hitung_ipk

def run_mahasiswa():
    try:
        print("\nMasukkan data mahasiswa:")
        print("----------------------------------------")
        nama = input("Nama Mahasiswa  : ")
        npm = input("NPM             : ")
        print("----------------------------------------")
        mhs = Mahasiswa(nama, npm)
        print(f"\nData Mahasiswa:")
        print("----------------------------------------")
        print(f"Nama Mahasiswa  : {mhs.nama}")
        print(f"NPM             : {mhs.npm}")
        print("----------------------------------------")
        print("\nMasukkan nilai (pisahkan dengan koma, contoh: 3.5,3.7,3.8,3.6):")
        nilai_input = input("Nilai           : ")
        try:
            nilai = [float(n.strip()) for n in nilai_input.split(",")]
            ipk = hitung_ipk(nilai)
            print("\nRingkasan Nilai:")
            print("----------------------------------------")
            print(f"Daftar Nilai    : {nilai}")
            print(f"IPK             : {ipk:.2f}")
            print("----------------------------------------")
            return True
        except ValueError:
            print("\nFormat nilai tidak valid!")
            return False
    except KeyboardInterrupt:
        print("\nOperasi dibatalkan!")
        return False 