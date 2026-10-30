# TEST CASE
## Program Rekap dan Analisis Nilai Matematika Kelas

**Nama:** Keyla Maharani  
**NIM:** 2225250083  
**Kelas:** 3E

## 1. Tujuan Pengujian

Pengujian dilakukan untuk memastikan program dapat membaca data siswa, memvalidasi nilai, menghitung statistik, menentukan ketuntasan, dan menyimpan laporan dengan benar.

KKM yang digunakan dalam proyek ini adalah 60.

## 2. Daftar Test Case

| No. | Skenario Pengujian | Input/Kondisi | Hasil yang Diharapkan | Hasil Aktual |
|---|---|---|---|---|
| 1 | Data nilai normal | 80, 70, 90 | Rata-rata 80, nilai tertinggi 90, nilai terendah 70 | Belum diuji |
| 2 | Nilai batas bawah | Nilai 0 | Data diterima | Belum diuji |
| 3 | Nilai batas atas | Nilai 100 | Data diterima | Belum diuji |
| 4 | Nilai melebihi batas | Nilai 105 | Data ditolak | Belum diuji |
| 5 | Nilai bukan angka | Nilai berupa huruf | Data ditolak | Belum diuji |
| 6 | File tidak ditemukan | File sumber tidak tersedia | Pesan kesalahan ditampilkan | Belum diuji |
| 7 | Data kosong | File tidak berisi data siswa | Pesan data kosong ditampilkan | Belum diuji |

## 3. Kriteria Keberhasilan

Pengujian dinyatakan berhasil apabila:
1. Program dapat membaca data siswa dengan benar.
2. Program dapat menerima nilai antara 0 sampai 100.
3. Program dapat menolak nilai yang tidak valid.
4. Perhitungan statistik menghasilkan nilai yang tepat.
5. Program dapat menentukan status ketuntasan berdasarkan KKM.
6. Program dapat menyimpan laporan hasil analisis.

## 4. Kesimpulan

Test case ini dirancang sebagai pedoman pengujian Program Rekap dan Analisis Nilai Matematika Kelas. Seluruh skenario akan dijalankan pada tahap implementasi proyek di Pertemuan 15.
