# Pertemuan 10 - String dan Pengolahan Teks

Nama: Rohelis  
NIM: 2225250064  
Kelas: 3B (S1 Pendidikan Matematika)  

---

## Tujuan
Mengolah dan menormalisasi data teks dengan string Python.

## Cara Menjalankan

Algoritma dan Pemrograman | Pertemuan 10  
S1 Pendidikan Matematika FKIP Universitas Sultan Ageng Tirtayasa | 2026/2027 Ganjil  

Jalankan perintah berikut di terminal:
```bash
python3 tugas/normalisasi_data_mahasiswa.py

ALGORITMA
Proses normalisasi teks dilakukan melalui tahapan berikut:
1. Normalisasi Nama:
   - Menggunakan .strip() untuk membuang spasi di awal dan akhir teks.
   - Menggunakan .split() dan " ".join() untuk merapikan spasi ganda antar kata menjadi spasi tunggal.
   - Menggunakan .title() untuk mengubah format huruf menjadi Title Case (huruf kapital di setiap awal kata).
2. Pembuatan Inisial:
   - Mengambil huruf pertama dari setiap kata pada nama yang telah dinormalisasi menggunakan indeks [0].
   - Menggabungkan dan mengubahnya menjadi huruf kapital menggunakan .upper().
3. Normalisasi Kode Kelas:
   - Membersihkan spasi berlebih, mengganti spasi antar kata menjadi tanda hubung (-) menggunakan .replace(" ", "-"), dan memastikan seluruh karakter menjadi huruf kapital dengan .upper().

TEST CASE
+-----------------------+------------------+--------------------------------------+----------+
| Input Nama            | Input Kode Kelas | Hasil yang Diharapkan / Aktual       | Status   |
+-----------------------+------------------+--------------------------------------+----------+
| aan hendrayana        | pmat a 2026      | Aan Hendrayana | PMAT-A-2026 | AH      | Berhasil |
| fATHIYYAH mUTHMAINNAH | kelas b          | Fathiyyah Muthmainnah | KELAS-B | FM | Berhasil |
| BUDI                  | pmtk 01          | Budi | PMTK-01 | B                 | Berhasil |
| siti nur aisyah       | kelas c          | Siti Nur Aisyah | KELAS-C | SNA     | Berhasil |
+-----------------------+------------------+--------------------------------------+----------+

REFLEKSI
- Masalah Teks yang Ditemukan:
  Data string dari pengguna sering kali tidak konsisten, seperti adanya spasi berlebih (whitespace),
  penggunaan huruf besar dan kecil yang tidak beraturan, serta spasi pada kode kelas yang memerlukan
  pemisah tanda hubung (-).
- Cara Memperbaikinya:
  Masalah tersebut diatasi dengan mengombinasikan built-in methods pada string Python secara berantai
  (method chaining), seperti .strip(), .split(), .replace(), .title(), dan .upper(), sehingga data teks
  menjadi bersih, seragam, dan siap diproses lebih lanjut.
===================================================================
"""

def normalisasi_nama(nama):
    # Menghilangkan spasi berlebih dan merapikan format ke Title Case
    return " ".join(nama.strip().split()).title()

def buat_inisial(nama):
    # Mengambil huruf pertama dari setiap kata pada nama yang sudah bersih
    nama_bersih = normalisasi_nama(nama)
    kata = nama_bersih.split()
    inisial = "".join([k[0] for k in kata])
    return inisial.upper()

def normalisasi_kode(kode):
    # Menghilangkan spasi di awal/akhir, mengganti spasi antar kata dengan "-", lalu kapital
    kode_bersih = " ".join(kode.strip().split())
    return kode_bersih.replace(" ", "-").upper()


# --- Pengujian Test Case Wajib ---
if __name__ == "__main__":
    test_cases = [
        ("aan hendrayana", "pmat a 2026"),
        ("fATHIYYAH mUTHMAINNAH", "kelas b"),
        ("BUDI", "pmtk 01"),
        ("siti nur aisyah", "kelas c")
    ]
    
    print("=== HASIL UJI TEST CASE WAJIB ===")
    for n_input, k_input in test_cases:
        nama_fix = normalisasi_nama(n_input)
        kode_fix = normalisasi_kode(k_input)
        inisial_fix = buat_inisial(n_input)
        
        # Menampilkan format Hasil Utama: Nama | Kode | Inisial
        print(f"{nama_fix} | {kode_fix} | {inisial_fix}")

    print("\n" + "="*40)
    print("=== PROGRAM UTAMA (INPUT MANUAL) ===")
    nama = input("Nama: ")
    kode = input("Kode kelas: ")
    
    # Tampilan Hasil Utama
    print("\nHasil Utama:")
    print(f"{normalisasi_nama(nama)} | {normalisasi_kode(kode)} | {buat_inisial(nama)}")