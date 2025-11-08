# 🔑 Rumus & Metrik Penting

## Metrik Klasifikasi (ML)

* **Akurasi (Accuracy):**
    * `(Jumlah Prediksi Benar) / (Total Data)`
    * `(TP + TN) / (TP + TN + FP + FN)`
    * Hati-hati: Tidak berguna jika datanya *imbalanced* (misal: 99% data "Karang Sehat", 1% "Karang Sakit").

* **Presisi (Precision):**
    * "Dari semua yang diprediksi **POSITIF**, berapa yang benar-benar **POSITIF**?"
    * `TP / (TP + FP)`
    * Penting jika **False Positive** merugikan (misal: memprediksi ada badai padahal tidak, membuat nelayan rugi tidak melaut).

* **Recall (Sensitivity):**
    * "Dari semua yang *seharusnya* **POSITIF**, berapa yang berhasil terdeteksi?"
    * `TP / (TP + FN)`
    * Penting jika **False Negative** berbahaya (misal: memprediksi tidak ada badai padahal ada, membahayakan nelayan).

* **F1-Score:**
    * Rata-rata harmonik dari Precision dan Recall.
    * `2 * (Precision * Recall) / (Precision + Recall)`
    * Metrik yang baik jika data *imbalanced*.

## Metrik NLP

* **TF-IDF (Term Frequency - Inverse Document Frequency):**
    * `TF(t,d) = (Jumlah kata 't' muncul di dokumen 'd') / (Total kata di dokumen 'd')`
    * `IDF(t,D) = log( (Total dokumen 'D') / (Jumlah dokumen yang mengandung kata 't') )`
    * `Skor TF-IDF = TF * IDF`
    * Intinya: Memberi skor tinggi pada kata yang *sering muncul di dokumen ini* TAPI *jarang muncul di dokumen lain* (kata unik/penting).

## Metrik Geospasial

* **Haversine Formula:**
    * Rumus untuk menghitung jarak antara dua titik di permukaan bola (bumi) berdasarkan lintang (latitude) dan bujur (longitude).
    * *Rumusnya rumit, tidak perlu dihafal, tapi tahu namanya dan kapan menggunakannya.*
