# 📓 Catatan Kuliah: Minggu 01 - Fondasi Data

**Dosen:** [Nama Dosen]
**Tanggal:** [Tanggal Kuliah]

## Poin Utama Kuliah

* **Apa itu "Digital Maritime"?** Ini bukan satu alat, tapi sebuah *pendekatan*. Menggunakan teknologi digital (AI, IoT, Web, Big Data) untuk memecahkan masalah di sektor kelautan.
* **Data adalah Aset Baru.** Dosen menekankan bahwa "minyak" baru di sektor maritim adalah data. Siapa yang menguasai data (data arus, ikan, polusi), dia yang memenangkan masa depan.
* **Tantangan Utama di Indonesia:** Data *fragmented* (tersebar). KKP punya data, BRIN punya, BIG punya. Tidak ada satu pintu. Inilah peluang kita sebagai *data scientist*.

## Istilah Kunci & Definisi

* **SST (Sea Surface Temperature):** Suhu Permukaan Laut. Data paling krusial untuk memprediksi *bleaching* (pemutihan karang) dan migrasi ikan.
* **Data Spasial vs. Tabular:**
    * **Tabular:** Data CSV/Excel biasa. Baris dan kolom (misal: Tanggal, Lokasi, Suhu).
    * **Spasial (GIS):** Data yang punya "bentuk" di peta (titik, garis, poligon).
* **API (Application Programming Interface):** "Pelayan" yang mengambilkan data untuk kita dari server (misal: API BMKG untuk cuaca).
* **Pandas (Python Library):** Alat utama kita. Anggap saja seperti "Excel yang dikendalikan kode." Objek utamanya disebut `DataFrame`.

## Catatan Tambahan

* Dosen memberi tips: Selalu cek `df.info()` dan `df.describe()` setelah me-load CSV. Ini langkah pertama *sanity check*.
* Mulai cari-cari portal data: Satu Data Indonesia, KKP, BRIN, BIG.
