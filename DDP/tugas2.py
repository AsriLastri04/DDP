print("================")
Nama_Pelanggan = input("Nama Pelanggan:")
Produk = input("Pilihan:")
if (Produk == "Kipas Angin"):
    Harga = 1000000
    print("Harga Produk: %i" % (Harga))
elif (Produk == "TV"):
    Harga = 2000000
    print("Harga Produk: %i" % (Harga))
elif (Produk == "Mesin Cuci"):
    Harga = 3000000
    print("Harga Produk: %i" % (Harga))
elif (Produk == "AC"):
    Harga = 4000000
    print("Harga Produk: %i" % (Harga))
else:
    Harga = 5000000
    print("Harga Produk: %i" % (Harga))
Jumlah_Beli = int(input("Jumlah Barang:"))
Harga_Kotor = Harga * Jumlah_Beli
print("Harga Kotor: %i" % (Harga_Kotor))
if (Produk == "Kulkas" and Jumlah_Beli>=5):
    Diskon = 0.20*Harga_Kotor
elif (Produk == "AC" and Jumlah_Beli>=3):
    Diskon = 0.10*Harga_Kotor
else:
    Diskon = 0.05*Harga_Kotor
PPN = Harga_Kotor-Diskon*0.10
print("PPN:%i" % (PPN))
Harga_Bersih = Harga_Kotor-Diskon+PPN
print("Harga Bersih:%i" % (Harga_Bersih))

