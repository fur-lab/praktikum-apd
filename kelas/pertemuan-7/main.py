# FUNGSI DAN PROSEDUR
# def nama_fungsi(parameter):
# pernyataan

# def perkenalan(): 
#     print("Halo")
#     print("Namaku Rafli")
#     input("Tekan ENTER untuk lanjut ...")

# perkenalan() # semua yang didalam indent terpanggil

# ada dua variabel : variabel global = diluar fungsi, variabel lokal = yang dideklar di dalam fungsi

# a = 45 + 5
# def perkalian():
#     x = 5 * 9
#     print(a)

# perkalian() # Hasilnya 50

# def perkenalan(nama):
#     print(f"Halo {nama}, selamat datang !")

# perkenalan("Rafli")

# def luas_persegi_panjang(panjang, lebar):
#     luas = panjang * lebar
#     print(f"Luas dari persegi pangjang adalah {luas}")
# luas_persegi_panjang(5, 7)

# def luas_persegi():
#     luas = sisi * sisi
#     return luas
# luas_persegi(8) # hasilnya error karena, tidak ada parameternya

# def luas_persegi(sisi):
#     luas = sisi * sisi # 4 * 4 = 16
#     return luas # fungsi return bakal : luas = 16
# # luas_persegi(f"luas persegi", luas_persegi(9) ) # belum selesai yng ini

# def volume_persegi(sisi):
#     volume = luas_persegi(sisi) * sisi  # v = 16.8.8 = 512
#     print ("Volume Persegi = ", volume)

# luas_persegi(4)
# volume_persegi(8)
# # hasilnya 512

# Fungsi Rekursif
# def faktorial(n): # faktorial itu buat memanggil dirinya sendiri sampai memanggil dirinya sampai tidak bisa dipanggil/habis (di base case, buat tempat berhenti)
# # Basis (Base Case): Kondisi berhenti
#     if n == 1 or n == 0:
#         return 1
# # Rekursi (Recursive Case): Fungsi memanggil dirinya sendiri
#     else:
#         return n * faktorial(n - 1)
# # Memanggil fungsi
# hasil = faktorial(7)
# print(f"Hasil dari 5! adalah: {hasil}")
# # Output:Hasil dari 5! adalah: 5040


# fungsi untuk menampilkan menu
def show_menu():
    print ("\n")
    print ("----------- MENU---------- ")
    print ("[1] Show Data")
    print ("[2] Insert Data")
    print ("[3] Edit Data")
    print ("[4] Delete Data")
    print ("[5] Exit")
    menu = input("PILIH MENU> ")
    print ("\n")
    if menu == "1":
        show_data()
    elif menu == "2":
        insert_data()
    elif menu == "3":
        edit_data()
    elif menu == "4":
        delete_data()
    elif menu == "5":
        exit()
    else:
        print ("Salah pilih!")

# Fungsi untuk menampilkan semua data
film = []
def show_data():
    if len(film) <= 0:
        print("Belum Ada data")
    else:
        print("ID | Judul Film")
    for indeks in range(len(film)):
        print(indeks, "|", film[indeks])

# Fungsi untuk menambah data
def insert_data():
    film_baru = input("Judul Film: ")
    film.append(film_baru)
    print("Film berhasil ditambahkan!")

# Fungsi untuk mengedit data
def edit_data():
    show_data()
    indeks = int(input("Inputkan ID film: "))
    if indeks >= len(film) or indeks < 0:
        print("ID salah")

    else:
        judul_baru = input("Judul baru: ")
        film[indeks] = judul_baru
        print("Film berhasil diupdate!")

# Fungsi untuk menghapus data
def delete_data():
    show_data()
    indeks = int(input("Inputkan ID film: "))
    if indeks >= len(film) or indeks < 0:
        print("ID salah")
    else:
        film.remove(film[indeks])
        print("Film berhasil dihapus!")

# fungsi untuk menampilkan menu
def show_menu():
    print ("\n")
    print ("----------- MENU---------- ")
    print ("[1] Show Data")
    print ("[2] Insert Data")
    print ("[3] Edit Data")
    print ("[4] Delete Data")
    print ("[5] Exit")
    menu = input("PILIH MENU> ")
    print ("\n")

    if menu == "1":
        show_data()
    elif menu == "2":
        insert_data()
    elif menu == "3":
        edit_data()
    elif menu == "4":
        delete_data()
    else:
        print('Tidak ada di menu')


while True:
    show_menu()


    # ERROR HANDLING
    harga = int(input("Masukan harga : "))
    print(harga)

    # try dan except buat nangkap errornya
    try:
        angka = int(input('Masukkan Angka : '))
    except ValueError:
        print('input yang anda masukkan bukan Integer (angka)') # sampai sini bener
    else:
        print(angka) # kalau mau nambahin
    finally:
        print("rawr") # tetap terprint walaupun error

    try:
        usn = input('Username yang diinginkan : ')
        if len(usn) < 5:
            raise ValueError('Nama Minimal Memiliki 5 karakter') # bikin error sendiri
    except ValueError as e:
        print(e)


# main.ipymb , buat jupiter notebook


# studi kasus 1
# try:








# # studi kasus 2
# try:
#     pw = input("Masukan pw : ")
#     if len(pw) < 8 :
#         raise ValueError("pw minimal 8 karakter ")
#     if not pw.isdigit():
#         raise ValueError("pw wajib ada angka")
# except ValueError as e:
#     print(e)

# # \t = buat menghilangkan spasi sebelum chara