# Membuat set

# buah = {"apel", "jeruk", "mangga", "apel"}
# buah = ([“apel”, “jeruk”, “mangga”, “apel”])
# print(buah) # ini pakai {} kesamping

# for i in buah:
#     # print(i) # tanpa {} dan kebawah
#     print(i, end = "") # tanpa {} dan kesamping tanpa spasi

# buat ubah tuple jadi set
# angka = {1,2,2,3,6,7,5,5,8,9,0}
# unik = set(angka)
# print(unik)

# Dictionary
# Daftar_buku = {
# "Buku1" : "Bumi Manusia", # Buku1 sebagai key dan seteralh : adalah value
# "Buku2" : "Laut Bercerita"
# }

# # print(Daftar_buku) # {} kesamping
# print(Daftar_buku["Buku1"]) # Bumu Manusia

# Biodata = {
# "Nama" : "Ananda Daffa Harahap",
# "NIM" : 2409106050,
# "KRS" : ["Pemrograman Web", "Struktur Data", "Basis Data"],
# "Mahasiswa_Aktif" : True,
# "Social Media" : {
# "Instagram" : "daffahrhap"
# }
# }

# print(Biodata) # {} kesamping

# for i in (Biodata):
    # print(i) # cuman key aja, karena i = indeks = key

    # for j in i:
    #     print(j) # kalau ini key, perhuruf kebawah

# tambahin .items() buat ngambil key dan value
# for i, j in Biodata.items(): # i dan j, kebawah, dan jika ada {} dan [] di dalamnya tetap terprint
#     print(i) # i = key
#     print(j) # j = value

# print(f"nama saya adalah {Biodata["Nama"]}") # Kalau key salah, dia bakal error
# print(f"Instagram : {Biodata["Social Media"]["Instagram"]}")
# print(f"nama saya adalah {Biodata.get("Nama")}")
# print(Biodata.get("Nama")) # Kalau pakai .get, dia bakal none

# Note : kalau pakai fungi -> .get , dll, harus pakai (). Contoh -> var.get(""). kalau -> var.get{} atau .get{} dia bakal salah/error

# Film = {
#     "Avenger" : "Action",
#     "Sherlock" : "Mystery",
#     "Conjuring" : "Horror"
# }

# Buat nambahin atau ganti value
# Film["ZombieLand"] = "Comedy" # buat nambahin
# Film.update({"Conjuring" : "Comedy"}) # buat update atau ganti data. Jika belum ada di dictionary, maka akan menambah data

# Kalau mau hapus, del, pop, clear
# hapus = Film
# del Film[]

# print(Film)

# Musik = {
#     "The Chainsmoker": ["All we Know", "The Paris"],
#     "Alan Walker": ["Alone", "Lily"],
#     "Neffex": ["Best of Me",['tes','halo'], "Memories"],
#     'Paramore' : ["Misery Business", "Ain't It Fun", 
#                 ['All We Know Is Falling',['Here We Go Again', 'My Heart']],'This Is Why' ]
# }

# print(Musik['Paramore'][2][1][0])

# angka = {} 
# print(type(angka)) # dict

# # buat set kosong
# angka = set()
# print(type(angka)) # set

# a = {10, 11, 12}
# b = {11, 13, 14}
# c = a | b # tanda & itu irisan dan hasilnya 11
# c = a | b # tanda | itu semua, dan karena set tidak ada yang duplikat
# print(c)

# Nilai = {
# "Matematika" : 80,
# "B. Indonesia" : 90,
# "B. Inggris" : 81
# }

# print("Nilai : ", Nilai.setdefault("Kimia", 70)) # hasilnya hanya 70