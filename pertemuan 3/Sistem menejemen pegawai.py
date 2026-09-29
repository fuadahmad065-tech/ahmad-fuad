# ==========================================
# KASUS 03: SISTEM MANAJEMEN PEGAWAI
# ==========================================

# INDUK 1: Pegawai & Gaji
class PegawaiGaji:
    def __init__(self, id_pegawai, nama, gaji):
        self.id_pegawai = id_pegawai
        self.nama = nama
        self.gaji = gaji

    def info_gaji(self):
        return f"ID: {self.id_pegawai} | Nama: {self.nama} | Gaji: Rp {self.gaji:,}"


# INDUK 2: Pegawai Proyek
class PegawaiProyek:
    def __init__(self, nama_proyek):
        self.nama_proyek = nama_proyek

    def info_proyek(self):
        return f"Proyek: {self.nama_proyek}"


# TURUNAN: Project Manager (Multiple Inheritance)
class ProjectManager(PegawaiGaji, PegawaiProyek):
    def __init__(self, id_pegawai, nama, gaji, nama_proyek):
        # Inisialisasi kedua induk
        PegawaiGaji.__init__(self, id_pegawai, nama, gaji)
        PegawaiProyek.__init__(self, nama_proyek)

    def cetak_semua(self):
        print(f"[PROJECT MANAGER]")
        print(f"  {self.info_gaji()}")
        print(f"  {self.info_proyek()}")
        print("-" * 30)


# INSTANSIASI OBJEK (3 Project Manager)
print("=== DATA PROJECT MANAGER ===\n")

pm1 = ProjectManager("PM-001", "Gita Permata", 15000000, "Aplikasi Mobile Banking")
pm2 = ProjectManager("PM-002", "Hendra Setiawan", 18000000, "Sistem ERP Perusahaan")
pm3 = ProjectManager("PM-003", "Indah Cahyani", 16500000, "Website E-Commerce")

# Cetak semua
pm1.cetak_semua()
pm2.cetak_semua()
pm3.cetak_semua()
