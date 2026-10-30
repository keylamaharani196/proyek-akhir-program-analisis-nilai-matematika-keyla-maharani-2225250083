# PROPOSAL PROYEK AKHIR
# PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA KELAS

## IDENTITAS MAHASISWA

- **Nama:** Keyla Maharani
- **NIM:** 2225250083
- **Kelas:** 3E
- **Program Studi:** S1 Pendidikan Matematika
- **Mata Kuliah:** Algoritma dan Pemrograman
- **Universitas:** Universitas Sultan Ageng Tirtayasa

---

## 1. Latar Belakang

Pengolahan nilai siswa merupakan salah satu kegiatan yang dilakukan dalam proses pembelajaran matematika. Guru perlu mengolah nilai siswa untuk mengetahui nilai rata-rata, nilai tertinggi, nilai terendah, serta jumlah siswa yang telah mencapai ketuntasan.

Apabila pengolahan nilai dilakukan secara manual, proses tersebut membutuhkan waktu dan berisiko terjadi kesalahan perhitungan. Oleh karena itu, diperlukan sebuah program sederhana menggunakan bahasa Python yang dapat membantu proses rekap dan analisis nilai matematika siswa secara otomatis.

Berdasarkan permasalahan tersebut, saya membuat proyek berjudul "Program Rekap dan Analisis Nilai Matematika Kelas".

## 2. Pengguna dan Tujuan Proyek

### A. Pengguna

Pengguna utama program ini adalah guru matematika yang membutuhkan bantuan untuk mengolah dan menganalisis nilai siswa.

### B. Tujuan

1. Mempermudah proses pengolahan data nilai matematika siswa.
2. Menghitung nilai rata-rata, tertinggi, dan terendah secara otomatis.
3. Mengetahui jumlah siswa yang tuntas dan tidak tuntas.
4. Mengurangi kesalahan dalam proses perhitungan nilai.
5. Menghasilkan laporan analisis nilai yang dapat disimpan dalam file.

## 3. Ruang Lingkup Proyek

Program ini memiliki batasan sebagai berikut:

1. Data siswa dibaca dari file teks.
2. Data terdiri atas nama siswa dan nilai matematika.
3. Nilai yang diterima berada pada rentang 0 sampai 100.
4. Batas ketuntasan atau KKM diasumsikan sebesar 60.
5. Program dijalankan melalui terminal menggunakan Python.
6. Hasil analisis disimpan dalam file teks.
7. Program menggunakan data contoh dan tidak menggunakan informasi pribadi siswa sebenarnya.

## 4. Fitur Program

### A. Fitur Wajib

1. Membaca data nama dan nilai siswa dari file `nilai_contoh.txt`.
2. Memvalidasi format data dan memastikan nilai berada pada rentang 0–100.
3. Menghitung nilai rata-rata, nilai tertinggi, dan nilai terendah.
4. Menentukan jumlah siswa yang tuntas dan tidak tuntas berdasarkan KKM 60.
5. Menampilkan hasil analisis dan menyimpan laporan ke file.

### B. Fitur Tambahan

Program dapat dikembangkan dengan menambahkan analisis nilai berdasarkan kategori tertentu apabila fitur utama sudah berjalan dengan baik.

## 5. Kebutuhan Fungsional dan Nonfungsional

### A. Kebutuhan Fungsional

- Program dapat membaca data siswa dari file teks.
- Program dapat memeriksa format data.
- Program dapat memvalidasi nilai siswa.
- Program dapat menghitung statistik nilai.
- Program dapat menentukan status ketuntasan siswa.
- Program dapat menampilkan hasil analisis.
- Program dapat menyimpan laporan ke dalam file teks.

### B. Kebutuhan Nonfungsional

- Program mudah dijalankan melalui VS Code.
- Program menggunakan bahasa pemrograman Python.
- Program memiliki pesan kesalahan yang mudah dipahami.
- Program menggunakan nama variabel dan fungsi yang jelas.
- Program dapat dijalankan kembali dengan data yang berbeda.

## 6. IPO (Input, Process, Output)

### A. Input

1. Nama siswa.
2. Nilai matematika siswa dari file `data/nilai_contoh.txt`.
3. KKM sebesar 60.

### B. Process

1. Membaca data siswa dari file.
2. Memeriksa format setiap baris data.
3. Memvalidasi nilai agar berada pada rentang 0–100.
4. Menyimpan data yang valid ke dalam struktur data.
5. Menghitung nilai rata-rata.
6. Menentukan nilai tertinggi dan terendah.
7. Menghitung jumlah siswa yang tuntas dan tidak tuntas.
8. Membuat laporan hasil analisis.

### C. Output

1. Daftar nama dan nilai siswa.
2. Nilai rata-rata kelas.
3. Nilai tertinggi.
4. Nilai terendah.
5. Jumlah siswa yang tuntas.
6. Jumlah siswa yang tidak tuntas.
7. File laporan `output/laporan.txt`.

## 7. Algoritma dan Pseudocode

```text
MULAI

Baca file nilai_contoh.txt

JIKA file tidak ditemukan
    Tampilkan pesan kesalahan
    SELESAI
AKHIR JIKA

Buat list kosong untuk menyimpan data siswa

UNTUK setiap baris dalam file
    Periksa format data
    Periksa apakah nilai berupa angka
    Periksa apakah nilai berada pada rentang 0–100

    JIKA data valid
        Simpan nama dan nilai siswa
    JIKA TIDAK
        Tampilkan pesan data tidak valid
    AKHIR JIKA
SELESAI PERULANGAN

JIKA tidak ada data valid
    Tampilkan pesan bahwa data kosong
    SELESAI
AKHIR JIKA

Hitung nilai rata-rata
Cari nilai tertinggi
Cari nilai terendah

Hitung jumlah siswa yang tuntas
Hitung jumlah siswa yang tidak tuntas

Tampilkan hasil analisis

Simpan laporan ke output/laporan.txt

SELESAI
```

## 8. Rancangan Struktur Program

Proyek akan menggunakan struktur folder sebagai berikut:

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

### Penjelasan File

- `README.md`: Berisi deskripsi proyek dan petunjuk menjalankan program.
- `proposal.md`: Berisi rancangan proyek.
- `.gitignore`: Mengatur file yang tidak perlu diunggah ke GitHub.
- `nilai_contoh.txt`: Menyimpan data contoh nilai siswa.
- `main.py`: Menjadi program utama.
- `data_io.py`: Mengatur proses membaca data dari file.
- `analisis.py`: Mengolah dan menghitung statistik nilai.
- `utilitas.py`: Berisi fungsi-fungsi pendukung.
- `test_case.md`: Berisi daftar pengujian program.
- `.gitkeep`: Menjaga folder output tetap tersedia di GitHub.

## 9. Rancangan Struktur Data

Struktur data yang digunakan dalam proyek ini adalah:

1. **List:** Digunakan untuk menyimpan kumpulan data nilai siswa.
2. **Dictionary:** Digunakan untuk menyimpan informasi nama dan nilai setiap siswa.
3. **String:** Digunakan untuk mengolah nama siswa dan menyusun laporan.
4. **File teks:** Digunakan untuk menyimpan data contoh dan hasil laporan.

Penggunaan struktur data tersebut bertujuan agar proses pengolahan data menjadi lebih teratur dan mudah dikelola.

## 10. Rancangan Fungsi Program

Program direncanakan memiliki beberapa fungsi berikut:

1. `baca_data()`: Membaca data siswa dari file.
2. `validasi_nilai()`: Memeriksa apakah nilai siswa valid.
3. `hitung_statistik()`: Menghitung rata-rata, nilai tertinggi, dan nilai terendah.
4. `tentukan_status()`: Menentukan status ketuntasan siswa.
5. `simpan_laporan()`: Menyimpan hasil analisis ke dalam file.
6. `main()`: Menjalankan keseluruhan proses program.

## 11. Rancangan Test Case

| No. | Pengujian | Input/Kondisi | Hasil yang Diharapkan |
|---|---|---|---|
| 1 | Data normal | Nilai 80, 70, 90 | Rata-rata 80 |
| 2 | Nilai batas bawah | Nilai 0 | Data diterima |
| 3 | Nilai batas atas | Nilai 100 | Data diterima |
| 4 | Nilai melebihi batas | Nilai 105 | Data ditolak |
| 5 | Data tidak valid | Nilai berupa huruf | Data ditolak |
| 6 | File tidak ditemukan | File sumber tidak tersedia | Pesan kesalahan ditampilkan |
| 7 | Data kosong | File tidak berisi data siswa | Pesan data kosong ditampilkan |

## 12. Pembagian Tugas

Proyek ini dikerjakan secara individu oleh:

**Nama:** Keyla Maharani  
**NIM:** 2225250083  
**Kelas:** 3E

Tanggung jawab pengerjaan meliputi:

1. Menentukan ide dan merancang proyek.
2. Menyusun proposal dan algoritma.
3. Membuat struktur folder dan program Python.
4. Melakukan pengujian program.
5. Memperbaiki kesalahan atau debugging.
6. Menyusun dokumentasi proyek.
7. Mengunggah hasil proyek ke GitHub.

## 13. Jadwal Pengerjaan

| Pertemuan | Kegiatan |
|---|---|
| Pertemuan 14 | Menentukan ide proyek, menyusun proposal, IPO, pseudocode, struktur program, dan test case. |
| Pertemuan 15 | Mengimplementasikan program Python, melakukan pengujian, debugging, dan melengkapi README. |
| Pertemuan 16 | Mempersiapkan presentasi dan melakukan demonstrasi program. |

## 14. Penutup

Program Rekap dan Analisis Nilai Matematika Kelas diharapkan dapat membantu proses pengolahan nilai siswa menjadi lebih mudah, cepat, dan sistematis.

Melalui proyek ini, konsep pemrograman Python seperti variabel, percabangan, perulangan, fungsi, list, dictionary, dan pengolahan file dapat diterapkan untuk menyelesaikan permasalahan sederhana dalam pembelajaran matematika.

Dengan demikian, proyek ini tidak hanya bertujuan menghasilkan sebuah program, tetapi juga menjadi sarana untuk menerapkan materi Algoritma dan Pemrograman yang telah dipelajari.
