# 📓 Catatan Kuliah: Minggu 02 - Pemetaan Web (GIS)

**Dosen:** [Nama Dosen]
**Tanggal:** [Tanggal Kuliah]

## Poin Utama Kuliah

* **Kenapa Web GIS?** Data maritim tidak ada artinya jika hanya angka di tabel. Harus divisualisasikan di peta. Web GIS = membawa peta itu ke *browser* agar semua orang bisa akses.
* **Raster vs. Vektor (PENTING!):**
    * **Raster:** Data berbasis piksel/grid (seperti gambar `.jpg`). Contoh: Citra satelit, peta batimetri (kedalaman).
    * **Vektor:** Data berbasis titik, garis, poligon (matematis). Contoh: Titik lokasi pelabuhan, garis rute kapal, poligon area konservasi.
* **Library Pilihan:**
    * **Folium (Python):** Mudah! Kita buat peta di Python, dia menghasilkan file `index.html` (Leaflet.js). Bagus untuk visualisasi cepat.
    * **Leaflet.js (JavaScript):** Sisi klien. Lebih fleksibel tapi harus *ngoding* JS. Folium sebenarnya hanya "pembungkus" Leaflet.

## Istilah Kunci & Definisi

* **GeoJSON:** Format standar untuk data vektor di web. Ini seperti file JSON biasa, tapi punya struktur spesifik untuk menyimpan "koordinat" dan "properti".
* **Shapefile (.shp):** Format data vektor yang sangat umum (dari ESRI/ArcGIS). Seringkali kita harus konversi `.shp` ke `.geojson`. `Geopandas` bisa melakukan ini.
* **CRS (Coordinate Reference System):** "Bahasa" yang dipakai peta. Paling umum: **WGS84 (EPSG:4326)**. Ini yang dipakai GPS. Penting untuk memastikan semua data kita pakai CRS yang sama.

## Catatan Tambahan

* `Geopandas` itu = Pandas + GIS. Dia punya `DataFrame` khusus (GeoDataFrame) yang ada kolom "geometry".
* Praktikum: Coba plot titik (koordinat) rumah sendiri di peta Folium. Lalu tambahkan *marker* dengan *popup*.
