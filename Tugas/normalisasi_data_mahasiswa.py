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