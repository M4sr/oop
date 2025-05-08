class Mahasiswa:
    def __init__(self, nama, npm):
        self.nama = nama
        self.npm = npm
    
    def get_info(self):
        return f"Nama: {self.nama}, NPM: {self.npm}" 