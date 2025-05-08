def hitung_ipk(nilai):
    """
    Menghitung IPK dari daftar nilai
    nilai: list of float (0-4)
    """
    if not nilai:
        return 0.0
    return sum(nilai) / len(nilai) 