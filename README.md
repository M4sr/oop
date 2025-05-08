# OOP Modular Project

## Deskripsi
Proyek ini adalah kumpulan latihan pemrograman berorientasi objek (OOP) dalam bahasa Python yang terstruktur secara modular. Setiap soal diletakkan dalam folder terpisah dan dapat dijalankan melalui satu program utama yang interaktif dan fleksibel.

## Fitur
- **Menu Interaktif:** Jalankan semua soal dari satu program utama (`main_program.py`).
- **Struktur Modular:** Setiap soal memiliki folder dan logika backend sendiri.
- **Input User:** Semua fitur menerima input dari pengguna.
- **Output Rapi:** Setiap menu menampilkan hasil yang terstruktur dan mudah dibaca.
- **Penanganan Error:** Program menangani input tidak valid dan KeyboardInterrupt dengan baik.

## Struktur Folder
```
├── main_program.py
├── soal1/
│   ├── math_ops.py
│   └── interface.py
├── soal2/
│   ├── mahasiswa/
│   │   ├── __init__.py
│   │   ├── profil.py
│   │   └── nilai.py
│   └── interface.py
├── soal3/
│   ├── hewan.py
│   └── interface.py
├── soal4/
│   ├── perpustakaan/
│   │   ├── __init__.py
│   │   ├── buku.py
│   │   └── anggota.py
│   └── interface.py
└── soal5/
    ├── user.py
    ├── course.py
    ├── registration.py
    └── interface.py
```

## Cara Menjalankan
1. **Clone repository ini:**
   ```bash
   git clone <url-repo-anda>
   cd <nama-folder-repo>
   ```
2. **Jalankan program utama:**
   ```bash
   python main_program.py
   ```
3. **Ikuti menu interaktif** untuk memilih dan menjalankan soal yang diinginkan.

## Daftar Soal
1. **Modul Matematika:**
   - Menghitung kuadrat dan pangkat tiga dari angka.
2. **Package Mahasiswa:**
   - Input data mahasiswa dan nilai, hitung IPK.
3. **Class Hewan:**
   - Pilih jenis hewan dan tampilkan suara.
4. **Package Perpustakaan:**
   - Input data buku dan anggota, pinjam buku.
5. **Sistem Pendaftaran Kursus:**
   - Input data kursus dan user, lakukan pendaftaran kursus.

## Kontributor
- Nama: ABDUL RAHMAN   
- NIM : 2110031806044

---

> **Catatan:**
> - Program ini dapat dijalankan di Windows, Linux, atau MacOS selama Python sudah terinstall.
> - Untuk keluar dari program, pilih menu `0` atau tekan `Ctrl+C`.
