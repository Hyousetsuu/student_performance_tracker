class Penilaian:
    """
    Menyimpan nilai quiz, tugas, UTS, dan UAS.
    Memiliki metode untuk menghitung nilai akhir berbobot.
    """

    def __init__(self, quiz=0, tugas=0, uts=0, uas=0):
        self.quiz = self._validate(quiz)
        self.tugas = self._validate(tugas)
        self.uts = self._validate(uts)
        self.uas = self._validate(uas)

    def _validate(self, nilai):
        if not (0 <= nilai <= 100):
            raise ValueError("Nilai harus antara 0–100.")
        return nilai

    def nilai_akhir(self):
        """Hitung nilai akhir berbobot"""
        return (
            self.quiz * 0.15
            + self.tugas * 0.25
            + self.uts * 0.25
            + self.uas * 0.35
        )
