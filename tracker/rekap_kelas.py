from .mahasiswa import Mahasiswa
from .penilaian import Penilaian

class RekapKelas:
    """
    Mengelola data banyak mahasiswa dan penilaian mereka.
    """

    def __init__(self):
        self.data = {}

    def tambah_mahasiswa(self, nim, nama):
        self.data[nim] = {"mhs": Mahasiswa(nim, nama), "nilai": Penilaian()}

    def set_hadir(self, nim, persen):
        if nim in self.data:
            self.data[nim]["mhs"].hadir_persen = persen
        else:
            print("❌ Mahasiswa tidak ditemukan.")

    def set_penilaian(self, nim, quiz, tugas, uts, uas):
        if nim in self.data:
            self.data[nim]["nilai"] = Penilaian(quiz, tugas, uts, uas)
        else:
            print("❌ Mahasiswa tidak ditemukan.")

    def predikat(self, nilai):
        """Konversi nilai akhir menjadi huruf"""
        if nilai >= 85:
            return "A"
        elif nilai >= 75:
            return "B"
        elif nilai >= 65:
            return "C"
        elif nilai >= 55:
            return "D"
        else:
            return "E"

    def rekap(self):
        """Kembalikan list of dict berisi data rekap"""
        records = []
        for nim, item in self.data.items():
            mhs = item["mhs"]
            nilai = item["nilai"].nilai_akhir()
            records.append({
                "NIM": mhs.nim,
                "Nama": mhs.nama,
                "Hadir (%)": mhs.hadir_persen,
                "Nilai Akhir": round(nilai, 2),
                "Predikat": self.predikat(nilai)
            })
        return records
