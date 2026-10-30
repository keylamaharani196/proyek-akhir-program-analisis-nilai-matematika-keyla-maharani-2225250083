
def baca_data(nama_file):
    data_siswa = []

    try:
        with open(nama_file, "r") as file:
            for nomor, baris in enumerate(file, start=1):
                bagian = baris.strip().split(",")

                if len(bagian) != 2:
                    print(f"Baris {nomor}: Format data tidak valid.")
                    continue

                nama = bagian[0].strip()

                try:
                    nilai = float(bagian[1].strip())
                except ValueError:
                    print(f"Baris {nomor}: Nilai harus berupa angka.")
                    continue

                if not nama:
                    print(f"Baris {nomor}: Nama tidak boleh kosong.")
                    continue

                if nilai < 0 or nilai > 100:
                    print(f"Baris {nomor}: Nilai harus 0 sampai 100.")
                    continue

                data_siswa.append({
                    "nama": nama,
                    "nilai": nilai
                })

    except FileNotFoundError:
        print("File data tidak ditemukan.")

    return data_siswa
