from .perpustakaan import Buku, Anggota

def run_perpustakaan():
    try:
        # Input buku
        print("\nMasukkan informasi buku:")
        print("----------------------------------------")
        judul = input("Judul Buku      : ")
        penulis = input("Penulis         : ")
        buku = Buku(judul, penulis)
        print("----------------------------------------")
        
        # Input anggota
        print("\nMasukkan informasi anggota:")
        print("----------------------------------------")
        nama_anggota = input("Nama Anggota    : ")
        anggota = Anggota(nama_anggota)
        print("----------------------------------------")
        
        # Pinjam buku
        anggota.pinjam_buku(buku)
        
        # Tampilkan informasi
        print("\nRingkasan Buku:")
        print("----------------------------------------")
        print(f"Judul Buku      : {buku.judul}")
        print(f"Penulis         : {buku.penulis}")
        print("----------------------------------------")
        print("\nRingkasan Anggota:")
        print("----------------------------------------")
        print(f"Nama Anggota    : {anggota.nama}")
        print(f"Jumlah Buku Dipinjam: {len(anggota.buku_dipinjam)}")
        print("----------------------------------------")
        return True
    except KeyboardInterrupt:
        print("\nOperasi dibatalkan!")
        return False 