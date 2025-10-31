class Penilaian:
    """
    Menyimpan nilai quiz, tugas, UTS, dan UAS.
    Memiliki property dengan validasi untuk nilai 0–100.
    """

    def __init__(self, quiz=0, tugas=0, uts=0, uas=0):
        self.quiz = quiz
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    @property
    def quiz(self):
        return self._quiz

    @quiz.setter
    def quiz(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Nilai Quiz harus antara 0–100.")
        self._quiz = value

    @property
    def tugas(self):
        return self._tugas

    @tugas.setter
    def tugas(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Nilai Tugas harus antara 0–100.")
        self._tugas = value

    @property
    def uts(self):
        return self._uts

    @uts.setter
    def uts(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Nilai UTS harus antara 0–100.")
        self._uts = value

    @property
    def uas(self):
        return self._uas

    @uas.setter
    def uas(self, value):
        if not (0 <= value <= 100):
            raise ValueError("Nilai UAS harus antara 0–100.")
        self._uas = value

    def nilai_akhir(self):
        """Hitung nilai akhir berbobot"""
        return (
            self.quiz * 0.15
            + self.tugas * 0.25
            + self.uts * 0.25
            + self.uas * 0.35
        )
