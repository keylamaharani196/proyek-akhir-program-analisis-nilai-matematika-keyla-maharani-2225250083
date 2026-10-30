
from data_io import baca_data
from analisis import hitung_statistik, tentukan_status
from utilitas import simpan_laporan


def main():
    print("======================================")
    print(" PROGRAM REKAP DAN ANALISIS NILAI")
    print("======================================")

    data_siswa = baca_data("data/nilai_contoh.txt")

    if not data_siswa:
        print("Tidak ada data siswa yang valid.")
        return

    statistik = hitung_statistik(data_siswa)
    status = tentukan_status(data_siswa, 60)

    print("\nHASIL ANALISIS NILAI")
    print("--------------------------------------")
    print("Jumlah siswa:", len(data_siswa))
    print("Nilai rata-rata:", statistik["rata_rata"])
    print("Nilai tertinggi:", statistik["tertinggi"])
    print("Nilai terendah:", statistik["terendah"])
    print("Jumlah siswa tuntas:", status["tuntas"])
    print("Jumlah siswa tidak tuntas:", status["tidak_tuntas"])

    simpan_laporan(data_siswa, statistik, status, "output/laporan.txt")
    print("\nLaporan berhasil disimpan.")


if __name__ == "__main__":
    main()
