# materi_reading.py

reading_content = """
## 📖 Modul Reading Comprehension: Ultimate Edition
Sesi Reading TOEFL memiliki 50 soal dengan waktu 55 menit. Anggap ini sebagai masalah optimasi waktu (Time Complexity: $O(1)$ per soal). Jangan me- *load* seluruh teks ke otak secara mentah-mentah; gunakan algoritma pencarian yang efisien.

### 1. ⚙️ Algoritma Penyelesaian (Teknik "Combat" Reading)
* **Skimming (Mencari Gagasan Utama):** Baca HANYA kalimat pertama dari setiap paragraf. Gagasan utama (Main Idea) hampir selalu di- *hardcode* di awal paragraf.
* **Scanning (Mencari Detail):** Jangan baca dari atas ke bawah. Lakukan *parsing* pada pertanyaannya dulu, ambil **kata kunci (keyword)**, lalu lakukan pencarian spesifik (*Ctrl+F* mental) di dalam teks.
* **Context Clues (Tebak Variabel):** Jika ada *Vocabulary* yang tidak diketahui, jangan panik. Anggap kata itu sebagai variabel kosong 'X'. Baca *string* kalimat sebelum dan sesudahnya untuk menebak apakah 'X' ini bermakna positif, negatif, atau netral.
* **Brute Force (Tembak Jawaban):** Tidak ada penalti (minus) di TOEFL. Jika waktu pada *timer* sisa 2 menit dan ada 10 soal tersisa, langsung eksekusi *brute force*: pilih satu huruf yang sama (misal B semua atau C semua).

### 2. 🎯 Pattern Recognition: Tipe Pertanyaan
* **Main Idea / Purpose:** Cari kesimpulan dari kalimat-kalimat pertama. Jawaban yang benar tidak terlalu spesifik (hanya mencakup 1 paragraf) dan tidak terlalu luas.
* **Stated Detail:** Jawaban PASTI ada di teks, tapi di- *compile* menggunakan **sinonim**. Cari kata kunci di teks, lalu cari padanan sinonimnya di pilihan jawaban.
* **Unstated Detail (NOT / EXCEPT):** Cari 3 pilihan yang *True* di teks, lalu eliminasi. Pilih satu-satunya yang bernilai *False*. (Peringatan: Tipe soal ini butuh *processing time* paling lama).
* **Inference (Kesimpulan Logis):** Jawabannya tersirat. Gunakan logika IF-THEN berdasarkan petunjuk tertulis di dalam teks.

---

### 3. 🗄️ Database Sinonim (Persamaan Kata)
Di TOEFL, jawaban yang benar 90% menggunakan sinonim dari teks. Hafalkan pemetaan data berikut:

| Kata di Teks (Vocabulary) | Sinonim (Pilihan Jawaban) | Arti |
| :--- | :--- | :--- |
| **Abundant** | Plentiful, Copious, Bountiful | Melimpah / Banyak |
| **Accelerate** | Speed up, Quicken, Hasten | Mempercepat |
| **Accumulate** | Gather, Collect, Amass | Mengumpulkan |
| **Adequate** | Sufficient, Enough, Satisfactory | Cukup / Memadai |
| **Alter** | Change, Modify, Adjust, Revise | Mengubah |
| **Ambiguous** | Unclear, Vague, Obscure | Ambigu / Tidak Jelas |
| **Anomaly** | Abnormality, Irregularity | Kejanggalan / Anomali |
| **Anticipate** | Expect, Predict, Foresee | Mengantisipasi / Memprediksi |
| **Beneficial** | Helpful, Advantageous, Favorable | Bermanfaat |
| **Crucial** | Essential, Vital, Critical, Important | Sangat penting |
| **Conceal** | Hide, Cover, Obscure, Mask | Menyembunyikan |
| **Detect** | Notice, Discover, Find, Identify | Mendeteksi / Menemukan |
| **Diverse** | Various, Different, Distinct | Beragam |
| **Emerge** | Appear, Arise, Surface | Muncul |
| **Flaw** | Defect, Fault, Error, Blemish | Cacat / Kesalahan / Bug |
| **Hazardous** | Dangerous, Perilous, Risky | Berbahaya |
| **Implement** | Execute, Apply, Carry out | Menerapkan / Melaksanakan |
| **Inevitable** | Unavoidable, Certain, Inescapable | Tidak bisa dihindari |
| **Negligible** | Insignificant, Minor, Trivial | Dapat diabaikan / Kecil |
| **Obsolete** | Outdated, Old-fashioned, Archaic | Kuno / Kedaluwarsa |
| **Prosper** | Thrive, Flourish, Succeed | Berkembang pesat / Makmur |
| **Retain** | Keep, Hold, Maintain, Preserve | Mempertahankan |
| **Significant** | Meaningful, Substantial, Notable | Penting / Signifikan |
| **Vast** | Huge, Massive, Immense, Enormous | Sangat luas / Besar |
| **Yield** | Produce, Generate, Provide, Surrender | Menghasilkan / Menyerah |

---

### 4. 🔄 Database Antonim (Lawan Kata)
Sangat krusial untuk soal *Inference* dan mendeteksi peralihan logika ketika ada kata penghubung seperti *However, On the other hand, Despite*:

| Kata Asli | Antonim (Lawan Kata) | Arti Perbandingan |
| :--- | :--- | :--- |
| **Abundant** (Melimpah) | **Scarce / Rare** (Langka) | Melimpah vs Langka |
| **Accelerate** (Mempercepat) | **Decelerate / Retard** (Memperlambat) | Cepat vs Lambat |
| **Ample** (Cukup/Luas) | **Insufficient / Meager** (Kurang) | Cukup vs Kurang |
| **Artificial** (Buatan) | **Genuine / Authentic** (Asli) | Buatan vs Asli |
| **Conceal** (Menyembunyikan)| **Reveal / Disclose** (Mengungkapkan) | Sembunyi vs Ungkap |
| **Diminish** (Menyusut) | **Expand / Enlarge** (Membesar) | Menyusut vs Membesar |
| **Dismantle** (Membongkar) | **Assemble / Construct** (Merakit) | Bongkar vs Rakit |
| **Prohibit** (Melarang) | **Permit / Allow** (Mengizinkan) | Larang vs Izinkan |
| **Rigid** (Kaku / Ketat) | **Flexible / Pliable** (Fleksibel) | Kaku vs Fleksibel |
| **Superficial** (Dangkal) | **Profound / Deep** (Mendalam) | Dangkal vs Mendalam |
| **Temporary** (Sementara) | **Permanent / Perpetual** (Permanen) | Sementara vs Abadi |
| **Transparent** (Tembus Pandang)| **Opaque** (Buram / Tidak tembus) | Bening vs Buram |
| **Vague** (Samar / Tidak Jelas) | **Explicit / Definite** (Jelas / Pasti) | Samar vs Jelas |

---

### 5. ⚠️ Confusing Words (Jebakan / Error Prone)
Kata-kata yang bunyinya sama/mirip (*Homophones*) yang sering menyebabkan *syntax error* di otak jika salah diterjemahkan. Sangat sering keluar di Listening Part A dan soal Vocabulary:

| Kata 1 | Arti | Kata 2 | Arti |
| :--- | :--- | :--- | :--- |
| **Affect** | Mempengaruhi (*Verb*) | **Effect** | Dampak/Hasil (*Noun*) |
| **Accept** | Menerima (*Verb*) | **Except** | Kecuali (*Preposition*) |
| **Adapt** | Menyesuaikan diri (*Verb*) | **Adopt** | Mengadopsi/Mengambil (*Verb*) |
| **Elicit** | Memancing reaksi (*Verb*) | **Illicit** | Ilegal / Dilarang (*Adjective*) |
| **Precede** | Mendahului / Sebelum (*Verb*) | **Proceed** | Melanjutkan (*Verb*) |
| **Principal** | Utama / Kepala Sekolah (*Noun/Adj*) | **Principle**| Prinsip / Aturan dasar (*Noun*) |
| **Compliment**| Pujian (*Noun/Verb*) | **Complement**| Pelengkap / Melengkapi (*Noun/Verb*) |
| **Allusion** | Kiasan / Referensi (*Noun*) | **Illusion** | Khayalan / Ilusi (*Noun*) |
| **Desert** | Gurun / Meninggalkan (*Noun/Verb*) | **Dessert** | Makanan penutup manis (*Noun*) |
| **Stationary**| Diam / Tidak bergerak (*Adjective*) | **Stationery**| Alat tulis kantor (*Noun*) |
| **Assure** | Meyakinkan orang lain (*Verb*) | **Ensure** | Memastikan sesuatu terjadi (*Verb*) |
| **Site** | Lokasi / Tempat (*Noun*) | **Sight** | Pemandangan / Penglihatan (*Noun*) |
| **Counsel** | Nasihat / Penasihat (*Noun/Verb*) | **Council** | Dewan / Komite (*Noun*) |
| **Capital** | Ibu kota / Modal (*Noun*) | **Capitol** | Gedung pusat pemerintahan (*Noun*) |
"""