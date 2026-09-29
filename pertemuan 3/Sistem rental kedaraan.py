# ==========================================
# KASUS 02: SISTEM RENTAL KENDARAAN
# ==========================================

# CLASS INDUK
class Kendaraan:
    def __init__(self, nama_penyewa, merk, tahun, kecepatan):
        self.nama_penyewa = nama_penyewa
        self.merk = merk
        self.tahun = tahun
        self.kecepatan = kecepatan

    def info_kendaraan(self):
        return f"{self.merk} ({self.tahun}) - {self.kecepatan} km/jam"


# TURUNAN 1: MOBIL
class Mobil(Kendaraan):
    def __init__(self, nama_penyewa, merk, tahun, kecepatan, jumlah_kursi):
        # Panggil inisialisasi induk
        super().__init__(nama_penyewa, merk, tahun, kecepatan)
        self.jumlah_kursi = jumlah_kursi

    def info_mobil(self):
        print(f"[MOBIL] Penyewa: {self.nama_penyewa}")
        print(f"        Kendaraan: {self.info_kendaraan()}")
        print(f"        Kursi: {self.jumlah_kursi}")
        print("-" * 30)


# TURUNAN 2: MOTOR
class Motor(Kendaraan):
    def __init__(self, nama_penyewa, merk, tahun, kecepatan, tipe_motor):
        super().__init__(nama_penyewa, merk, tahun, kecepatan)
        self.tipe_motor = tipe_motor

    def info_motor(self):
        print(f"[MOTOR] Penyewa: {self.nama_penyewa}")
        print(f"        Kendaraan: {self.info_kendaraan()}")
        print(f"        Tipe: {self.tipe_motor}")
        print("-" * 30)


# INSTANSIASI OBJEK (3 Penyewa)
print("=== DATA RENTAL KENDARAAN ===\n")

rental1 = Mobil("Dedi Kurniawan", "Toyota Avanza", 2022, 180, 7)
rental2 = Motor("Eka Putri", "Honda Vario", 2023, 120, "Skutik")
rental3 = Mobil("Fajar Ramadhan", "Honda Brio", 2021, 160, 5)

# Cetak semua
rental1.info_mobil()
rental2.info_motor()
rental3.info_mobil()