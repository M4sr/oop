class Anggota:
    def __init__(self, nama):
        self.nama = nama
        self.buku_dipinjam = []
    
    def pinjam_buku(self, buku):
        self.buku_dipinjam.append(buku)
    
    def get_info(self):
        return f"Nama: {self.nama}, Jumlah buku dipinjam: {len(self.buku_dipinjam)}"