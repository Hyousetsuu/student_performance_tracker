from tracker import RekapKelas, build_markdown_report, build_html_report, save_text

def main():
    rekap = RekapKelas()

    while True:
        print("\n=== Student Performance Tracker ===")
        print("1) Tambah mahasiswa")
        print("2) Ubah presensi")
        print("3) Ubah nilai")
        print("4) Lihat rekap")
        print("5) Simpan laporan Markdown")
        print("6) Simpan laporan HTML")
        print("7) Tampilkan mahasiswa nilai < 70")
        print("8) Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nim = input("NIM: ")
            nama = input("Nama: ")
            rekap.tambah_mahasiswa(nim, nama)
            print("✅ Mahasiswa ditambahkan.")

        elif pilihan == "2":
            nim = input("NIM: ")
            try:
                persen = float(input("Persentase hadir (0–100): "))
                rekap.set_hadir(nim, persen)
                print("✅ Presensi diperbarui.")
            except ValueError:
                print("❌ Input tidak valid, masukkan angka 0–100.")

        elif pilihan == "3":
            nim = input("NIM: ")
            try:
                quiz = float(input("Nilai Quiz: "))
                tugas = float(input("Nilai Tugas: "))
                uts = float(input("Nilai UTS: "))
                uas = float(input("Nilai UAS: "))
                rekap.set_penilaian(nim, quiz, tugas, uts, uas)
                print("✅ Nilai diperbarui.")
            except ValueError:
                print("❌ Masukkan nilai numerik 0–100.")

        elif pilihan == "4":
            data = rekap.rekap()
            if not data:
                print("Belum ada data mahasiswa.")
            else:
                print("\nNIM\tNama\tHadir\tNilai\tPredikat")
                for r in data:
                    print(f"{r['NIM']}\t{r['Nama']}\t{r['Hadir (%)']}%\t{r['Nilai Akhir']}\t{r['Predikat']}")

        elif pilihan == "5":
            data = rekap.rekap()
            content = build_markdown_report(data)
            save_text("out/report.md", content)
            print("📄 Laporan Markdown disimpan di out/report.md")

        elif pilihan == "6":
            data = rekap.rekap()
            html = build_html_report(data)
            save_text("out/report.html", html)
            print("🌐 Laporan HTML disimpan di out/report.html")

        elif pilihan == "7":
            data = [r for r in rekap.rekap() if r["Nilai Akhir"] < 70]
            if not data:
                print("✅ Tidak ada mahasiswa dengan nilai di bawah 70.")
            else:
                print("\nMahasiswa dengan nilai < 70:")
                for r in data:
                    print(f"{r['NIM']} - {r['Nama']} ({r['Nilai Akhir']}) [{r['Predikat']}]")

        elif pilihan == "8":
            print("👋 Keluar dari program.")
            break

        else:
            print("Pilihan tidak valid, coba lagi.")

if __name__ == "__main__":
    main()
