Nama_pasien = input("Masukkan nama pasien: ")   #variabel untuk menyimpan nama pasien
Tinggi_badan = float(input("Masukan tinggi badan pasien (dalam cm): ")) #variabel untuk menyimpan tinggi badan pasien
Berat_badan = float(input("Masukan berat badan pasien (dalam kg): ")) #variabel untuk menyimpan berat badan pasien


beratIdeal = (Tinggi_badan - 100) #rumus berat badan ideal
isKelebihan = Berat_badan > beratIdeal #variabel dengan tipe data boolean
statusList = ["Berat Badan Ideal", "Kelebihan Berat Badan"] #list untuk status berat badan

print("-------------------------------------------")
print("|          HASIL CEK BERAT BADAN          |")
print("-------------------------------------------")
print(f"| Nama Pasien  : {Nama_pasien:<20}     |")
print(f"| Tinggi Badan : {Tinggi_badan:<3} cm                 |")
print(f"| Berat Badan  : {Berat_badan:<5} kg                 |")
print(f"| Berat Ideal  : {beratIdeal:<5} kg                 |")
print(f"| Status       : {statusList[isKelebihan]:<21}    |")
print("-------------------------------------------")



