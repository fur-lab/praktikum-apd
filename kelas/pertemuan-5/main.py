# nested
# praktikum = ["apd", "orsikom", "jarkom",["RPL", "basis data"]]
# print(praktikum)


# for i in praktikum:
#     print(i)

# kalau mau ngambil yang nested
# print(praktikum[3][1])

# append
# praktikum1 = ["apd", "orsikom","jarkom", "rpl"]
# praktikum1.append("basdat")
# print(praktikum1)

# insert
# praktikum1.insert(2, "basdat")
# print(praktikum1)

# kalau mau nambahkan data saat input
# inputNilai = input("Matkul : ")
# praktikum1.append(inputNilai)
# print(praktikum1)

# mau hapus del, remove, pop
# del praktikum1[3] # rpl yang dihapus
# praktikum1.remove("apd") # apd yang dihapus
# ambil_praktikum1 = praktikum1.pop(1) # orsikom yang dihapus
# print(praktikum1)

# slicing/memotong
# urutan = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(urutan[0:10:5]) # start:step:stop kalau 2 star:stop kalau 1 stop

# list mahasiswa
# mahasiswa = [["Daffa", "Dante", "Santoso"], ["Pernanda", "Triya", "Ahnaf"]]
# # perulangan for untuk mendapatkan semua elemen
# for i in mahasiswa:
#     for j in i :
#         print(j)
# i dan j merupakan variabel sementara / temporary, kita dapat menggantinya dengan apa saja asal sesuai dengan syarat nama variabel

# tuple
# matkul = ("kalku", "basing")
# # print(type(matkul)) # cek tipe data
# pelajaran = ("fisika") # bukan tuple dan kalo mau tambahin koma diakhir
# print(pelajaran)

# key & value, kayak berangkas dan kunci
# tugas = ('rangkuman', 'arduino','scrapping')

# beri key setiap values, jumlah indeks dan key
# (PTI, orsikom, basisdata) = tugas
# print(PTI)

tugas = ('rangkuman', 'arduino','scrapping', "rrr")
(PTI, orsikom, *basisdata) = tugas