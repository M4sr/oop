from .hewan import Anjing

class Kucing:
    def bersuara(self):
        return "Meong!"

def run_hewan():
    try:
        print("\n=== PILIH JENIS HEWAN ===")
        print("1. Anjing")
        print("2. Kucing")
        print("3. Lainnya (custom)")
        pilihan = input("Pilih hewan (1/2/3): ")
        print("----------------------------------------")
        if pilihan == "1":
            hewan = Anjing()
            jenis = "Anjing"
            suara = hewan.bersuara()
        elif pilihan == "2":
            hewan = Kucing()
            jenis = "Kucing"
            suara = hewan.bersuara()
        elif pilihan == "3":
            jenis = input("Masukkan jenis hewan: ")
            suara = input("Masukkan suara hewan: ")
        else:
            print("Pilihan tidak valid!")
            return False
        print("\nRingkasan Hewan:")
        print("----------------------------------------")
        print(f"Jenis Hewan    : {jenis}")
        print(f"Suara          : {suara}")
        print("----------------------------------------")
        return True
    except KeyboardInterrupt:
        print("\nOperasi dibatalkan!")
        return False 