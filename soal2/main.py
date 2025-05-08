from mahasiswa import Mahasiswa, hitung_ipk

def main():
    # Membuat objek mahasiswa
    mhs = Mahasiswa("John Doe", "2021001")
    print(mhs.get_info())
    
    # Menghitung IPK
    nilai = [3.5, 3.7, 3.8, 3.6]
    ipk = hitung_ipk(nilai)
    print(f"IPK: {ipk:.2f}")

if __name__ == "__main__":
    main() 