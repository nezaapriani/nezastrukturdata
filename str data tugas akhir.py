# Aplikasi Manajemen Nilai Mahasiswa

data_mahasiswa = [
    ["NEZA CEWEK JAEHYUN", 85],
    ["DIAH", 78],
    ["TIARA", 90]
]

while True:
    print("\n====================================")
    print(" APLIKASI MANAJEMEN NILAI MAHASISWA")
    print("====================================")
    print("1. Tampilkan Data")
    print("2. Tambah Data")
    print("3. Ubah Data")
    print("4. Hapus Data")
    print("5. Cari Data")
    print("6. Urutkan Data Berdasarkan Nilai")
    print("7. Hitung Rata-rata Nilai")
    print("8. Keluar")

    pilihan = input("Pilih menu (1-8): ")
    if pilihan == "1":
        print("\nDaftar Mahasiswa")
        for data in data_mahasiswa:
            print("Nama:", data[0], "| Nilai:", data[1])
    elif pilihan == "2":
        nama = input("Masukkan nama mahasiswa: ")
        nilai = int(input("Masukkan nilai mahasiswa: "))
        data_mahasiswa.append([nama, nilai])
        print("Data berhasil ditambahkan.")
    elif pilihan == "3":
        nama = input("Masukkan nama mahasiswa yang akan diubah: ")
        ditemukan = False
        for data in data_mahasiswa:
            if data[0].lower() == nama.lower():
                data[0] = input("Masukkan nama baru: ")
                data[1] = int(input("Masukkan nilai baru: "))
                ditemukan = True
                print("Data berhasil diubah.")
                break
        if not ditemukan:
            print("Data tidak ditemukan.")
    elif pilihan == "4":
        nama = input("Masukkan nama mahasiswa yang akan dihapus: ")
        for data in data_mahasiswa:
            if data[0].lower() == nama.lower():
                data_mahasiswa.remove(data)
                print("Data berhasil dihapus.")
                break
        else:
            print("Data tidak ditemukan.")

    elif pilihan == "5":
        nama = input("Masukkan nama mahasiswa yang dicari: ")
        for data in data_mahasiswa:
            if data[0].lower() == nama.lower():
                print("Data ditemukan:")
                print("Nama :", data[0])
                print("Nilai:", data[1])
                break
        else:
            print("Data tidak ditemukan.")

    elif pilihan == "6":
        data_mahasiswa.sort(key=lambda x: x[1], reverse=True)
        print("Data berhasil diurutkan berdasarkan nilai tertinggi.")
    elif pilihan == "7":
        total = 0
        for data in data_mahasiswa:
            total += data[1]
        rata_rata = total / len(data_mahasiswa)
        print("Rata-rata nilai mahasiswa =", rata_rata)

    elif pilihan == "8":
        print("Program selesai. Terima kasih.")
        break
    else:
        print("Pilihan tidak valid!")