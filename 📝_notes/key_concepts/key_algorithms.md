# 🔑 Algoritma Kunci

* **Logistic Regression (Klasifikasi):**
    * Meskipun namanya "regresi", ini adalah algoritma **klasifikasi**.
    * Cara kerja: Menghitung probabilitas (antara 0 dan 1) apakah sebuah data masuk ke Kategori A atau B. Menggunakan fungsi Sigmoid.
    * Bagus sebagai *baseline model* karena cepat dan mudah diinterpretasi.

* **K-Means (Clustering - Unsupervised):**
    * Cara kerja: Kita tentukan `K` (jumlah cluster), misal 3.
    * 1. Algoritma menaruh 3 "pusat" (centroid) secara acak.
    * 2. Semua titik data dihitung jaraknya & "bergabung" ke centroid terdekat.
    * 3. Posisi centroid di-update ke tengah-tengah anggotanya.
    * 4. Ulangi langkah 2-3 sampai posisi centroid tidak berubah.
    * Contoh Maritim: Mengelompokkan kapal nelayan (data GPS) ke dalam `K`=3 "zona tangkap" utama.

* **CNN (Convolutional Neural Network - Visi Komputer):**
    * Cara kerja: Berbeda dari ML biasa, CNN tidak melihat gambar sebagai "piksel".
    * 1. **Convolution Layer:** "Filter" (kernel) kecil digeser ke seluruh gambar untuk mendeteksi fitur (tepi, sudut, tekstur).
    * 2. **Pooling Layer:** Mereduksi ukuran gambar (downsampling) agar lebih efisien, hanya menyimpan informasi terpenting.
    * 3. **Fully Connected Layer:** Sama seperti ML biasa di akhir, untuk membuat keputusan klasifikasi.
    * Contoh Maritim: Filter pertama mendeteksi "tekstur kasar", filter kedua "warna putih", filter ketiga "bentuk bercabang" -> CNN menyimpulkan: "Karang Acropora".

* **LDA (Latent Dirichlet Allocation - NLP):**
    * Algoritma *Topic Modeling* (Unsupervised).
    * Cara kerja: Kita beri `K`=5 topik.
    * LDA akan membaca *semua* dokumen dan menghasilkan dua hal:
        1.  Setiap "topik" adalah kumpulan kata (misal: Topik 1 = 30% "kapal", 20% "rempah", 15% "belanda").
        2.  Setiap "dokumen" adalah campuran topik (misal: Dokumen A = 60% Topik 1, 40% Topik 3).
    * Contoh Maritim: Menganalisis arsip VOC untuk menemukan 5 "topik utama" yang dibicarakan.
