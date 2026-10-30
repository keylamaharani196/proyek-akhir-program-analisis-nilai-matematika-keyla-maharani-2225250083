
def hitung_statistik(data_siswa):
    daftar_nilai = [siswa["nilai"] for siswa in data_siswa]

    rata_rata = sum(daftar_nilai) / len(daftar_nilai)
    tertinggi = max(daftar_nilai)
    terendah = min(daftar_nilai)

    return {
        "rata_rata": round(rata_rata, 2),
        "tertinggi": tertinggi,
        "terendah": terendah
    }


def tentukan_status(data_siswa, kkm):
    tuntas = 0
    tidak_tuntas = 0

    for siswa in data_siswa:
        if siswa["nilai"] >= kkm:
            tuntas += 1
        else:
            tidak_tuntas += 1

    return {
        "tuntas": tuntas,
        "tidak_tuntas": tidak_tuntas
    }
