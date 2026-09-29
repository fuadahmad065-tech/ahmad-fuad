# ==========================================
# KASUS 01: SISTEM PENDAFTARAN MAHASISWA
# ==========================================

class Mahasiswa:
    # INISIALISASI: Constructor __init__
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.nilai = 0  # Default nilai awal

    # LOGIKA KELULUSAN: cek status >= 75
    def status(self):
        if self.nilai >= 75:
            return "LULUS"
        else:
            return "TIDAK LULUS"

    # CETAK PROFIL
    def cetak_profil(self):
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print(f"Nilai   : {self.nilai}")
        print(f"Status  : {self.status()}")
        print("-" * 30)


# INSTANSIASI OBJEK (3 Mahasiswa)
print("=== DATA MAHASISWA ===\n")

mhs1 = Mahasiswa("Andi Pratama", "2024001", "Teknik Informatika")
mhs2 = Mahasiswa("Bunga Lestari", "2024002", "Sistem Informasi")
mhs3 = Mahasiswa("Candra Wijaya", "2024003", "Teknik Komputer")

# Set nilai masing-masing
mhs1.nilai = 85  # Lulus
mhs2.nilai = 70  # Tidak Lulus
mhs3.nilai = 90  # Lulus

# Cetak semua profil
mhs1.cetak_profil()
mhs2.cetak_profil()
mhs3.cetak_profil()