pegawai_1 = ['Ahmad','Islam',4000000,2]
pegawai_2 = ['Alex','kristen protestan', 6000000,5]

tunjangan_jabatan = 20/100

if (pegawai_1[3] <= 2):
        tunjangan_keluarga = 10/100 * pegawai_1[2]
elif (pegawai_1[3] >2):
    tunjangan_keluarga = 20/100 * pegawai_1[2]
else:     
    tunjnagan_keluarga = 0                                                       

gaji_kotor = pegawai_1[2] + tunjangan_jabatan * pegawai_1[2] + tunjangan_keluarga

zakat_profesi = 0
if (pegawai_1[1] == "Islam" and gaji_kotor >= 6000000):
    zakat_profesi = 2.5/100 * gaji_kotor


gaji_bersih =  gaji_kotor - zakat_profesi


print('SLIP GAJI PT. XYZ')
print('------------------')
print('Nama Pegawai\t\t:',pegawai_1[0])
print('Agama\t\t\t:',pegawai_1[1])
print('Jumlah Anak\t\t:',pegawai_1[3])
print('Gaji Pokok\t\t: Rp.',pegawai_1[2])
print('Tunjangan Jabatan\t: Rp.',tunjangan_jabatan*pegawai_1[2])
print('Tunjangan Keluarga\t: Rp.',tunjangan_keluarga)
print('Gaji Kotor\t\t: Rp.', gaji_kotor)
print('Zakat Profesi\t\t: Rp.', zakat_profesi)
print('Take Home Pay\t\t: Rp.', gaji_bersih)


if(pegawai_2[3] <= 2):
        tunjangan_keluarga = 10/100 * pegawai_2[2]
elif(pegawai_2[3] > 2):
    tunjangan_keluarga = 20/100 * pegawai_2[2]
else:
   tunjangan_keluarga = 0


gaji_kotor = pegawai_2[2] + tunjangan_jabatan* pegawai_2[2] + tunjangan_keluarga


zakat_profesi = 0
if(pegawai_2[1] == "Islam" and gaji_kotor > 6000000):
    zakat_profesi = 2,5/100 * gaji_kotor
else:
    zakat_profesi = 0


gaji_bersih =  gaji_kotor - zakat_profesi

print('SLIP GAJI PT. XYZ')
print('------------------')
print('Nama Pegawai\t\t:',pegawai_2[0])
print('Agama\t\t\t:',pegawai_2[1])
print('Jumlah Anak\t\t:',pegawai_2[3])
print('Gaji Pokok\t\t: Rp.',pegawai_2[2])
print('Tunjangan Jabatan\t: Rp.',tunjangan_jabatan*pegawai_2[2])
print('Tunjangan Keluarga\t: Rp.',tunjangan_keluarga)
print('Gaji Kotor\t\t: Rp.', gaji_kotor)
print('Zakat Profesi\t\t: Rp.', zakat_profesi)
print('Take Home Pay\t\t: Rp.', gaji_bersih)
