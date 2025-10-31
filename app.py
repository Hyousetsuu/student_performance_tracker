from tracker import RekapKelas, build_markdown_report, build_html_report, save_text
import csv

def muat_data_dari_csv(rekap):
    """Memuat data mahasiswa, kehadiran, dan nilai dari file CSV"""
    try:
        with open("data/attendance.csv", newline="", encoding="utf-8") as f1, \
             open("data/grades.csv", newline="", encoding="utf-8") as f2:
            hadir_reader = csv.DictReader(f1)
            nilai_reader = csv.DictReader(f2)

            for row in hadir_reader:
                nim = row["NIM"]
                nama = row["Nama"]
                hadir = float(row["Hadir"])
                rekap.tambah_mahasiswa(nim, nama)
                rekap.set_hadir(nim, hadir)

            for row in nilai_reader:
                nim = row["NIM"]
                quiz = float(row["Quiz"])
                tugas = float(row["Tugas"])
                uts = float(row["UTS"])
                uas = float(row["UAS"])
                rekap.set_penilaian(nim, quiz, tugas, uts, uas)

        print("✅ Data berhasil dimuat dari CSV.")
    except FileNotFoundError:
        print("❌ File CSV tidak ditemukan di folder data/.")


def main():
    rekap = RekapKelas()

    while True:
        print("\n=== Student Performance Tracker ===")
        print("1) Muat data dari CSV")
        print("2) Tambah mahasiswa")
        print("3) Ubah presensi")
        print("4) Ubah nilai")
        print("5) Lihat rekap")
        print("6) Simpan laporan Markdown")
        print("7) Simpan laporan HTML")
        print("8) Tampilkan mahasiswa nilai < 70")
        print("9) Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            muat_data_dari_csv(rekap)

        elif pilihan == "2":
            nim = input("NIM: ")
            nama = input("Nama: ")
            rekap.tambah_mahasiswa(nim, nama)
            print("✅ Mahasiswa ditambahkan.")

        elif pilihan == "3":
            nim = input("NIM: ")
            persen = float(input("Persentase hadir (0–100): "))
            rekap.set_hadir(nim, persen)

        elif pilihan == "4":
            nim = input("NIM: ")
            quiz = float(input("Nilai Quiz: "))
            tugas = float(input("Nilai Tugas: "))
            uts = float(input("Nilai UTS: "))
            uas = float(input("Nilai UAS: "))
            rekap.set_penilaian(nim, quiz, tugas, uts, uas)

        elif pilihan == "5":
            data = rekap.rekap()
            print("\nNIM\tNama\tHadir\tNilai\tPredikat")
            for r in data:
                print(f"{r['NIM']}\t{r['Nama']}\t{r['Hadir (%)']}%\t{r['Nilai Akhir']}\t{r['Predikat']}")

        elif pilihan == "6":
            data = rekap.rekap()
            content = build_markdown_report(data)
            save_text("out/report.md", content)
            print("📄 Laporan disimpan ke out/report.md")

        elif pilihan == "7":
            data = rekap.rekap()
            html = build_html_report(data)
            save_text("out/report.html", html)
            print("🌐 Laporan disimpan ke out/report.html")

        elif pilihan == "8":
            data = [r for r in rekap.rekap() if r["Nilai Akhir"] < 70]
            if not data:
                print("✅ Tidak ada mahasiswa dengan nilai di bawah 70.")
            else:
                print("\nMahasiswa dengan nilai < 70:")
                for r in data:
                    print(f"{r['NIM']} - {r['Nama']} ({r['Nilai Akhir']}) [{r['Predikat']}]")

        elif pilihan == "9":
            print("👋 Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
