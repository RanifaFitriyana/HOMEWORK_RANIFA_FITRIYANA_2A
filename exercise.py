barang = []

def tambah_data():
    nama = str(input("Masukkan Nama Barang : "))
    stok = int(input("Masukkan Stok Barang : "))
    barang_new = {'nama' : nama.capitalize(), 'stok' : stok}
    barang.append(barang_new)
    print("<<< Data Berhasil Ditambahkan >>>")


def edit_data():
    edit = int(input("Edit Data Index Ke = "))
    if edit >= len(barang):
        print("Index Tidak Ada Dalam Data")
        return
    
    nama_baru = str(input("Masukkan Nama Barang Baru : "))
    stok_baru = int(input("Masukkan Jumlah Stok Baru : "))

    barang[edit]["nama"] = nama_baru.capitalize()
    barang[edit]["stok"] = stok_baru
    print("<<< Data Berhasil Diubah >>>")
  

def hapus_data():
    hapus = int(input("Hapus Data Index Ke = "))
    barang.pop(hapus) 
    print("<<< Data Berhasil Dihapus >>>")


def cari_data():
    nama_cari = str(input("Cari Nama Barang: "))
    print("=========== Hasil Pencarian ==========")
    for i in barang:
        if i['nama'].capitalize() == nama_cari.capitalize():
            print('•',i['nama'],'--> Stok :',i['stok'])
            return
    print("-------- Data Tidak Ditemukan --------")

  
def tampil_data():
    print("========== Toko Elektronik ===========")
    for i in barang:
        print('•',i['nama'],'--> Stok : ',i['stok'])
    if not barang:
        print("--------- Data Barang Kosong ---------")
 

def jumlah_data():
    print("Jumlah Data Tersimpan :",len(barang), "Barang")




     