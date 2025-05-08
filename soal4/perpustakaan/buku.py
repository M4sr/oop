class Buku:
    def __init__(self, judul, penulis):
        self.judul = judul
        self.penulis = penulis
    
    def get_info(self):
        return f"Judul: {self.judul}, Penulis: {self.penulis}" 