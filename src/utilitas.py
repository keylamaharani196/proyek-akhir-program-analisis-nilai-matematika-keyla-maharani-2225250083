
def simpan_laporan(data_siswa, statistik, status, nama_file):
    try:
        with open(nama_file, "w") as file:
            file.write("LAPORAN ANALISIS NILAI MATEMATIKA\n")
            file.write("====================================\n\n")

            file.write("DAFTAR NILAI SISWA\n")

            for siswa in data_siswa:
                file.write(
                    f'{siswa["nama"]}: {siswa["nilai"]}\n'
                )

            file.write("\nHASIL ANALISIS\n")
            file.write("------------------------------------\n")
            file.write(f'Jumlah siswa: {len(data_siswa)}\n')
            file.write(f'Nilai rata-rata: {statistik["rata_rata"]}\n')
            file.write(f'Nilai tertinggi: {statistik["tertinggi"]}\n')
            file.write(f'Nilai terendah: {statistik["terendah"]}\n')
            file.write(f'Siswa tuntas: {status["tuntas"]}\n')
            file.write(f'Siswa tidak tuntas: {status["tidak_tuntas"]}\n')

    except OSError:
        print("Laporan gagal disimpan.")
