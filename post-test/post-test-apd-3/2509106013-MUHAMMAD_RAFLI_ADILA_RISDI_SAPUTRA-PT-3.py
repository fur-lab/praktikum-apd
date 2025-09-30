print("-" * 55)
print("Selamat datang dan selamat berbelanja di toko kami! ")
print("-" * 55)

Member = input("Apakah anda sudah menjadi member? (ya/tidak): ")
print("-" * 55)
username = "Rafli"
password = "013"

# daftar harga
Daftar_harga = ("""
Silahkan pilih Item yang anda beli : 
1. Baju = Rp. 100.000 
2. Celana panjang = Rp. 150.000 
3. Sepatu = Rp. 300.000 
""")

# Item
Baju = 100000
Celana_panjang = 150000
Sepatu = 300000

# Perhitungan diskon
Diskon = 0.15

# Percabangan apakah user member
if Member == "ya":
    Login_Username = input("Masukkan username member anda : ")
    Login_Password = input("Masukan password member anda : ")
    User_Member = True if Login_Username == username and Login_Password == password else print("Username atau password salah!") 
    
    # Percabangan jika user member
    if User_Member == True:
        print("-" * 55)
        print(Daftar_harga)
        pilihan_Member = int(input("Masukan hanya nomor saja :"))
        print("-" * 55)

        # Peercabangan pilihan member
        if pilihan_Member == 1:
            Jumlah = int(input("Masukan jumlah item : "))
            print("-" * 55)
            Jumlah_baju = Baju * Jumlah
            Harga_Diskon_baju = Jumlah_baju * Diskon
            Total_Baju = Jumlah_baju - Harga_Diskon_baju
            print(f"Harga total baju : Rp." ,Jumlah_baju)
            print(f"Harga Diskon : Rp.", Harga_Diskon_baju)
            print(f"Total Pembayaran : Rp.", Total_Baju)
            print("-" * 55)
            print("Terima kasih sudah berbelanja di toko kami !")
            print("-" * 55)

        elif pilihan_Member == 2:
            Jumlah = int(input("Masukan jumlah item : "))
            print("-" * 55)
            Jumlah_celana_panjang = Celana_panjang * Diskon
            Harga_Diskon_Celana_Panjang = Jumlah_celana_panjang * Diskon
            Total_Celana_Panjang = Jumlah_celana_panjang - Harga_Diskon_Celana_Panjang
            print(f"Harga total Celana Panjang : Rp." ,Jumlah_celana_panjang)
            print(f"Harga Diskon : Rp.", Harga_Diskon_Celana_Panjang)
            print(f"Total Pembayaran : Rp.", Total_Celana_Panjang)
            print("-" * 55)
            print("Terima kasih sudah berbelanja di toko kami !")
            print("-" * 55)

        elif pilihan_Member == 3:
            Jumlah = int(input("Masukan jumlah item : "))
            print("-" * 55)
            Jumlah_Sepatu = Sepatu * Diskon
            Harga_Diskon_Sepatu = Jumlah_Sepatu * Diskon
            Total_Sepatu = Jumlah_Sepatu - Harga_Diskon_Sepatu
            print(f"Harga total Sepatu : Rp." ,Jumlah_Sepatu)
            print(f"Harga Diskon : Rp.", Harga_Diskon_Sepatu)
            print(f"Total Pembayaran : Rp.", Total_Sepatu)
            print("-" * 55)
            print("Terima kasih sudah berbelanja di toko kami !")
            print("-" * 55)
        else:
            print("TIDAK ADA DALAM DAFTAR!")
    else:
        print("Gagal login")
else:
    print(Daftar_harga)
    pilihan_bukan_Member = int(input("Masukan hanya nomor saja :"))
    print("-" * 55)

    # Percabangan pilihan bukan member
    if pilihan_bukan_Member == 1:
        Jumlah = int(input("Masukan jumlah item : "))
        print("-" * 55)
        Jumlah_baju = Baju * Jumlah
        print(f"Total Pembayaran : Rp.", Jumlah_baju)
        print("-" * 55)
        print("Terima kasih sudah berbelanja di toko kami !")
        print("-" * 55)

    elif pilihan_bukan_Member == 2:
        Jumlah = int(input("Masukan jumlah item : "))
        print("-" * 55)
        Jumlah_celana_panjang = Celana_panjang * Jumlah
        print(f"Total Pembayaran : Rp.", Jumlah_celana_panjang)
        print("-" * 55)
        print("Terima kasih sudah berbelanja di toko kami !")
        print("-" * 55)
    
    elif pilihan_bukan_Member == 3:
        Jumlah = int(input("Masukan jumlah item : "))
        print("-" * 55)
        Jumlah_Sepatu = Sepatu * Jumlah
        print(f"Total Pembayaran : Rp.", Jumlah_Sepatu)
        print("-" * 55)
        print("Terima kasih sudah berbelanja di toko kami !")
        print("-" * 55)
    else:
        print("TIDAK ADA DALAM DAFTAR!")