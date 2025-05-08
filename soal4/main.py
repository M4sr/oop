from perpustakaan import Buku, Anggota

def main():
    # Membuat beberapa buku
    buku1 = Buku("Python Programming", "John Smith")
    buku2 = Buku("Data Science", "Jane Doe")
    
    # Membuat anggota
    anggota = Anggota("Alice")
    
    # Menampilkan informasi buku
    print("Daftar Buku:")
    print(buku1.get_info())
    print(buku2.get_info())
    
    # Menampilkan informasi anggota
    print("\nInformasi Anggota:")
    print(anggota.get_info())

if __name__ == "__main__":
    main() 