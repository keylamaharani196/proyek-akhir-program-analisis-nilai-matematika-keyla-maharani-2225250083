# Program Rekap dan Analisis Nilai Matematika Kelas

## Identitas Mahasiswa

- **Nama:** Keyla Maharani
- **NIM:** 2225250083
- **Kelas:** 3E
- **Program Studi:** S1 Pendidikan Matematika
- **Universitas:** Universitas Sultan Ageng Tirtayasa

## Deskripsi Proyek

Program Rekap dan Analisis Nilai Matematika Kelas merupakan program sederhana berbasis Python yang dibuat untuk membantu guru mengolah dan menganalisis nilai matematika siswa secara otomatis.

Program membaca data nama dan nilai siswa dari file teks, memvalidasi data, menghitung statistik nilai, menentukan ketuntasan siswa, serta menyimpan hasil analisis ke dalam file laporan.

## Fitur Program

1. Membaca data siswa dari file teks.
2. Memvalidasi nilai siswa dalam rentang 0–100.
3. Menghitung nilai rata-rata.
4. Menentukan nilai tertinggi dan terendah.
5. Menghitung jumlah siswa tuntas dan tidak tuntas.
6. Menyimpan hasil analisis ke file laporan.

**KKM:** 60 (asumsi proyek).

## Teknologi yang Digunakan

- Bahasa pemrograman Python.
- Visual Studio Code.
- Git dan GitHub.
- File teks untuk penyimpanan data dan laporan.

## Struktur Folder

```text
proyek-akhir-program-analisis-nilai-matematika-keyla-maharani-2225250083/
│
├── README.md
├── proposal.md
├── .gitignore
│
├── data/
│   └── nilai_contoh.txt
│
├── src/
│   ├── main.py
│   ├── data_io.py
│   ├── analisis.py
│   └── utilitas.py
│
├── tests/
│   └── test_case.md
│
└── output/
    └── .gitkeep
```

## Cara Menjalankan Program

Program akan dijalankan melalui terminal VS Code menggunakan perintah:

```bash
python src/main.py
```

## Pengujian Program

Pengujian direncanakan mencakup beberapa kondisi:

1. Data nilai normal.
2. Nilai batas bawah (0).
3. Nilai batas atas (100).
4. Nilai melebihi batas (105).
5. Nilai berupa huruf.
6. File tidak ditemukan.
7. File kosong.

Hasil pengujian akan dilengkapi setelah program diimplementasikan dan dijalankan pada Pertemuan 15.

## Dokumentasi

Dokumentasi berupa hasil pengujian dan tangkapan layar program akan ditambahkan setelah tahap implementasi.

## Referensi dan Bantuan AI

Penyusunan rancangan proyek dilakukan dengan mempelajari materi Pertemuan 14 dan menggunakan bantuan AI untuk membantu menyusun ide, struktur, dan dokumentasi proyek. Implementasi dan pengujian program akan dilakukan serta dipahami secara mandiri.

## Penutup

Proyek ini diharapkan dapat membantu proses rekapitulasi dan analisis nilai matematika siswa serta menjadi penerapan materi Algoritma dan Pemrograman menggunakan Python.
