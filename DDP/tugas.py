# Pegawai 1 Ahmad muslim memiliki gaji pokok  Rp.4.000.00 dan  memiliki dua orang anak.#
#Pegawai 2 Alex beragama Kristen Protestan memiliki gaji pokok  Rp. 6.000.000 dan memiliki 5 orang anak.#
#Pegawai 1
print("Pegawai Pertama")
nama_pegawai = "Ahmad"
agama = "islam"
gaji_pokok = 4000000
tunjangan_jab = 0.2 * gaji_pokok
print(tunjangan_jab)
#tunjangankeluarga
jumlahanak = 2
if (jumlahanak == 2):
    print(0.1 * gaji_pokok)
elif(jumlahanak >= 2):
    print(0.2 * gaji_pokok)
else:
    print(0)
tunjangankeluarga = 400000
# Jika jumlah anak maksimal 2 anak, tunjangan keluarga 10% dari gaji pokok
#Jika jumlah anak lebih dari 2 orang, tunjangan keluarga 20% dari gaji pokok
#Jika belum mempunyai anak, belum dapat tunjangan keluarga
gaji_kotor = gaji_pokok + tunjangankeluarga + tunjangan_jab
zakat_profesi = (0, 0.025)[agama == "islam" and gaji_kotor >= 6000000]*gaji_kotor
gaji_bersih = gaji_kotor - zakat_profesi
print(gaji_kotor)
print(gaji_bersih)
print('tugas 1 DDP')
print('='*30)
print("Nama :", nama_pegawai)
print("\n Agama :", agama)
print("\n Jumlah Anak :",jumlahanak)
print("\n Gaji Pokok :",gaji_pokok)
print("\n Tunjangan Jabatan :",tunjangan_jab)
print("\n Tunjangan keluarga :",tunjangankeluarga)
print("\n Gaji Kotor :",gaji_kotor)
print("\n Zakat Profesi :",zakat_profesi)
print("\n Gaji Bersih :",gaji_bersih)












#Pegawaikedua
print("Pegawai Kedua")
nama_pegawai1 = "Alex"
agama1 = "Kristen Protestan"
gaji_pokok1 = 6000000
tunjangan_jab1 = 0.2 * gaji_pokok1
print(tunjangan_jab1)
#tunjangankeluarga1
jumlah_anak1 = 5
# Jika jumlah anak maksimal 2 anak, tunjangan keluarga 10% dari gaji pokok
#Jika jumlah anak lebih dari 2 orang, tunjangan keluarga 20% dari gaji pokok
#Jika belum mempunyai anak, belum dapat tunjangan keluargaterm
if (jumlah_anak1 == 2):
    print(0.1 * gaji_pokok1)
elif(jumlah_anak1 >=  2):
    print(0.2 * gaji_pokok1)
else:
    print(0)
tunjangankeluarga1 = 1200000
gaji_kotor1 = gaji_pokok1 + tunjangan_jab1 + tunjangankeluarga1
zakat_profesi1 = (0, 0.025)[agama1 == "islam" and gaji_kotor1 >= 6000000]*gaji_kotor1
gaji_bersih1 = gaji_kotor1 - zakat_profesi1
print(gaji_kotor1)
print(gaji_bersih1)
print('='*30)
print("Nama ", nama_pegawai1)
print("\n Agama :", agama1)
print("\n Jumlah Anak : ",jumlah_anak1)
print("\n Gaji Pokok : ",gaji_pokok1)
print("\n Tunjangan Jabatan : ",tunjangan_jab1)
print("\n Tunjangan keluarga : ",tunjangankeluarga1)
print("\n Gaji Kotor :", gaji_kotor1)
print("\n Zakat Profesi :",zakat_profesi1)
print("\n Gaji Bersih :",gaji_bersih1)
