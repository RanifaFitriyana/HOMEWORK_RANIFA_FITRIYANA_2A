import exercise as exe

print("Selamat Datang di Program Manajemen Stok Barang!")
print("Pilihan :")
print("1. Tambah Data Barang")
print("2. Edit Data")
print("3. Hapus Data Barang")
print("4. Cari Data")
print("5. Tampilkan Data Barang")
print("6. Tampilkan Jumlah Data")
print("7. Keluar")

while True:
    pilihan = input("\nMasukkan Pilihan Anda : ")

    if pilihan == '1':
        exe.tambah_data()
    elif pilihan == '2':
        exe.edit_data()
    elif pilihan == '3':
        exe.hapus_data()
    elif pilihan == '4':
        exe.cari_data()
    elif pilihan == '5':
        exe.tampil_data()
    elif pilihan == '6':
        exe.jumlah_data()
    elif pilihan == '7':
        print("Terimakasih Telah Menggunakan Program Ini :)\n")
        break
    else:
        print("Pilihan Yang Anda Masukkan Salah, Coba Lagi!")