class Mahasiswa:
    """
    Representasi data mahasiswa.
    Memiliki atribut NIM, nama, dan persentase kehadiran.
    """

    def __init__(self, nim, nama, hadir_persen=0):
        self.nim = nim
        self.nama = nama
        self._hadir_persen = 0
        self.hadir_persen = hadir_persen

    @property
    def hadir_persen(self):
        return self._hadir_persen

    @hadir_persen.setter
    def hadir_persen(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Persentase hadir harus antara 0–100.")
        self._hadir_persen = value

    def info(self):
        """Menampilkan informasi mahasiswa"""
        return f"{self.nim} - {self.nama} ({self.hadir_persen}%)"
