# 🎯 TOEFL Simulation & Learning Platform

Sebuah aplikasi berbasis web yang dirancang untuk simulasi ujian TOEFL secara mandiri. Platform ini mengintegrasikan modul pembelajaran materi dengan sistem ujian digital yang interaktif, lengkap dengan pengatur waktu otomatis dan penilaian instan.

---

## 🌟 Fitur Utama

* **📚 Modul Pembelajaran:** Menyediakan materi terstruktur untuk bagian *Reading* dan *Grammar* guna membantu persiapan sebelum ujian.
* **⏱️ Real-time Live Timer:** Sistem penghitung waktu mundur yang akurat untuk memberikan pengalaman ujian yang realistis.
* **🔀 Randomized Questioning:** Soal diambil secara acak dari database untuk memastikan variasi tes setiap kali sesi baru dimulai.
* **📊 Automatic Scoring:** Penilaian otomatis segera setelah ujian selesai, mencakup skor per kategori dan total jawaban benar.
* **📑 Review Key:** Fasilitas untuk meninjau kembali kunci jawaban lengkap setelah pengerjaan selesai.

---

## 🛠️ Arsitektur Proyek (Modular Structure)

Aplikasi ini dibangun dengan struktur file yang terorganisir untuk mempermudah pembaruan data:

| Nama File | Deskripsi |
| :--- | :--- |
| `app.py` | Logika aplikasi utama dan manajemen antarmuka Streamlit. |
| `data_grammar.py` | Database soal Structure & Written Expression. |
| `data_reading.py` | Database soal Reading Comprehension beserta teks bacaan. |
| `materi_grammar.py` | File pendukung berisi konten edukasi tata bahasa. |
| `materi_reading.py` | File pendukung berisi strategi dan materi bacaan. |

---

## 🧪 Tech Stack

* **Language:** [Python 3.x](https://www.python.org/)
* **Frontend Framework:** [Streamlit](https://streamlit.io/)
* **Add-ons:** `streamlit-autorefresh` (untuk sinkronisasi waktu).
* **Logic:** Session State management, Time calculations, & Data randomization.

---

## 🚀 Panduan Instalasi

1. **Clone Repository:**
   ```bash
   git clone [https://github.com/RayanHakim/TOEFL-Simulation.git](https://github.com/RayanHakim/TOEFL-Simulation.git)
   cd TOEFL-Simulation
