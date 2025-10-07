# Untuk mengimport os agar bisa membersihkan layar
import os

# Deklarasi untuk Login
username = "Rafli"
password = "013"

# daftar harga
Daftar_harga = ("""
Silahkan pilih Item yang anda beli : 
1. Baju = Rp. 100.000 
2. Celana panjang = Rp. 150.000 
3. Sepatu = Rp. 300.000 
4. Selesai
""")

# Logika belanja
Belanja_lagi = "y"

# Item
Baju = 100000
Celana_panjang = 150000
Sepatu = 300000

# Perhitungan diskon
Diskon = 0.15


# Perulangan belanja
while Belanja_lagi ==  "y":

    Percobaan = 0
    Max_Percobaan = 3
    User_Member = False
    Total_Belanja_Sementara = 0

    # Bersihkan layar
    os.system("cls")
    
    # Menampilkan Menu
    print("-" * 55)
    print("Selamat datang di toko kami! ")
    print("-" * 55)
    Member = input("Apakah anda sudah menjadi member? (y/n): ")
    print("-" * 55)
    
    # Percabangan apakah user member
    if Member == "y":
        while Percobaan < Max_Percobaan:
            Login_Username = input("Masukkan username member anda : ")
            Login_Password = input("Masukan password member anda : ")

            if Login_Username == "Rafli" and Login_Password == "013":
                print(f"Selamat datang {Login_Username}")
                print("Selamat Berbelanja")
                User_Member = True
                break

            else:
                Percobaan += 1
                print("Username atau Password salah !!!")
        
    elif Member == "n":
        print("-" * 55)
        print("Selamat Berbelanja")
        print("-" * 55)
    
    else:
        print("-" * 55)
        print("Selamat Berbelanja")
        print("-" * 55)

    # Perulangan keranjang
    while True:
        os.system("cls")

        print(Daftar_harga)
        print(f"Total Keranjang Saat Ini: Rp. {Total_Belanja_Sementara:,}") 
        print("-" * 55)
        pilihan = int(input("Masukan hanya nomor saja :"))
        
        if pilihan == 1:
            Total_Belanja_Sementara += Baju
            print("Baju berhasil ditambahkan ke keranjang.")

        elif pilihan == 2:
            Total_Belanja_Sementara += Celana_panjang
            print("Celana panjang berhasil ditambahkan ke keranjang.")

        elif pilihan == 3:
            Total_Belanja_Sementara += Sepatu
            print("Sepatu berhasil ditambahkan ke keranjang.")

        elif pilihan == 4:
            break

        else:
            print("Item tidak ada dalam menu !!!")
            input("Tekan enter untuk melanjutkan...")
            continue
    
    os.system("cls")

    if User_Member:
        Jumlah_Diskon = Total_Belanja_Sementara * Diskon
        Total_Setelah_Diskon = Total_Belanja_Sementara - Jumlah_Diskon
        print(f"Total belanja sebelum diskon: Rp. {Total_Belanja_Sementara:,}")
        print(f"Potongan diskon 15%: Rp. {Jumlah_Diskon:,}")
        print(f"Total yang harus dibayar: Rp. {Total_Setelah_Diskon:,}")

    else:
        print(f"Total yang harus dibayar: Rp. {Total_Belanja_Sementara:,}")

    Belanja_lagi = input("Apakah ingin melakukan transaksi baru? (y/n): ")
    os.system("cls")

print("Program telah selesai. Terima kasih sudah berbelanja!")