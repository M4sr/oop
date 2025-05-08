from .math_ops import square, cube

def run_matematika():
    try:
        print("\n=== MODUL MATEMATIKA ===")
        print("----------------------------------------")
        angka = float(input("Masukkan Angka  : "))
        print("----------------------------------------")
        hasil_kuadrat = square(angka)
        hasil_pangkat_tiga = cube(angka)
        print("Hasil Perhitungan:")
        print("----------------------------------------")
        print(f"Angka           : {angka}")
        print(f"Kuadrat         : {hasil_kuadrat}")
        print(f"Pangkat Tiga    : {hasil_pangkat_tiga}")
        print("----------------------------------------")
        return True
    except ValueError:
        print("\nInput tidak valid! Masukkan angka.")
        return False
    except KeyboardInterrupt:
        print("\nOperasi dibatalkan!")
        return False 