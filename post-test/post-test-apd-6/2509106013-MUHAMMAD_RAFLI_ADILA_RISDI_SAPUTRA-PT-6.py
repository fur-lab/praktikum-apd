# impor os agar membersihkan layar
import os

# username, password dan status admin buat masuk ke menu admin
Username = "Rafli"
Password = "013"
Admin = False

# Logika buat Program berlanjut
Program ="y"

# daftar
Daftar_Mobil = [
    [1, "Toyota", "Yaris", 2011, "Bekas", 130000000],
    [2, "Honda", "City", 2005, "Bekas", 70000000],
    [3, "Daihatsu", "Ayla", 2025, "Baru", 160000000]
]

while Program == "y":
    percobaan = 0
    max_percobaan = 3

    os.system("cls")
    print("="*75)
    print("Selamat datang di Dealer Amanah !")
    print("="*75)

    User = input("Sebelum lanjut, anda akan masuk sebagai (admin / pelanggan) : ")
    print("="*75)
    
    # Percabangan user
    if User == "admin":
        os.system("cls")
        while percobaan < max_percobaan:
            Login_Username = input("Masukkan username Admin : ")
            Login_Password = input("Masukan password Admin : ")

            if Login_Username == "Rafli" and Login_Password == "013":
                    print(f"Selamat datang admin {Login_Username}")
                    print("="*75)
                    Admin = True
                    break

            else:
                percobaan += 1
                print("Username atau Password salah !!!")
                    

        while Admin == True :
                        os.system("cls")
                        print("Apa yang ingin anda lakukan hari ini ?")
                        print("="*75)
                        print("1. Tambah Mobil") # Create
                        print("2. Tampilkan semua daftar Mobil") # Read
                        print("3. Ubah data") # Update
                        print("4. Hapus data Mobil dari daftar") # Delete
                        print("5. Logout")
                        print("="*75)
                        pilihan = input("Masukan pilihan anda (1-5) : ")

                        if pilihan == "1": # Create
                            os.system("cls")
                            print("="*75)
                            print("Tambah Mobil")
                            print("="*75)

                            last_id = 0

                            if Daftar_Mobil: # Agar tau kalau Daftar_Mobil ada isinya
                                for Mobil in Daftar_Mobil:
                                    if Mobil[0] > last_id:
                                        last_id = Mobil[0]
                            id_baru = last_id + 1

                            Merek = input("Masukkan Merek: ")
                            Model = input("Masukkan Model: ")
                            Tahun = int(input("Masukkan Tahun (Angka): ")) 
                            Kondisi = input("Masukkan Kondisi (Baru/Bekas): ")
                            Harga = int(input("Masukkan Harga (Angka, tanpa titik/koma): ")) 

                            Mobil = [id_baru, Merek, Model, Tahun, Kondisi, Harga]
                            Daftar_Mobil.append(Mobil)

                        elif pilihan == "2": # Read
                            os.system("cls")
                            print("="*75)
                            print("Daftar Mobil di dealer Amanah")
                            print("="*75)

                            # Tabel
                            print("=" * 75)
                            print(f"{'ID':<5} | {'Merek':<10} | {'Model':<10} | {'Tahun':<6} | {'Kondisi':<7} | {'Harga (Rp.)':<20}")
                            print("=" * 75)
                                
                            # Loop untuk daftar mobil
                            for mobil in Daftar_Mobil:
                                print(f"{mobil[0]:<5} | {mobil[1]:<10} | {mobil[2]:<10} | {mobil[3]:<6} | {mobil[4]:<7} | {mobil[5]:<20} ")

                                print("=" * 75)
                            
                            input("Tekan ENTER untuk kembali ke menu...")

                        elif pilihan == "3": # Update
                            os.system("cls")
                            id_Ubah = int(input("Masukan ID Mobil yang ingin anda ubah (dalam bentuk angka): "))
                            ada = False

                            for i in range(len(Daftar_Mobil)):
                                if Daftar_Mobil[i][0] == id_Ubah:
                                    ada = True

                                    print(f"Anda akan mengedit: {Daftar_Mobil[i][1]} {Daftar_Mobil[i][2]}")
                                    harga_baru_edit = int(input("Masukkan Harga (Angka): "))
                                    
                                    Daftar_Mobil[i][5] = harga_baru_edit  # Kedalam kolom ke-5
                                    
                                    print("Harga mobil berhasil diubah !")
                                    break 
            
                            input("Tekan ENTER untuk kembali ke menu...")

                        elif pilihan == "4": # Delete
                            os.system("cls")
                            print("=" * 75)
                            print(f"{'ID':<5} | {'Merek':<10} | {'Model':<10} | {'Tahun':<6} | {'Kondisi':<7} | {'Harga (Rp.)':<20}")
                            print("=" * 75)

                            for mobil in Daftar_Mobil: 
                                print(f"{mobil[0]:<5} | {mobil[1]:<10} | {mobil[2]:<10} | {mobil[3]:<6} | {mobil[4]:<7} | {mobil[5]:<20} ")

                                
                            print("="*75)
                            id_hapus = int(input("Silahkan masukan no. mobil yang ingin anda hapus (dalam bentuk angka): "))
                            print("="*75)
                            
                            ada = False

                            for i in range(len(Daftar_Mobil)):
                                    if Daftar_Mobil[i][0] == id_hapus:
                                        ada = True
                                        
                                        nama_mobil = f"{Daftar_Mobil[i][1]} {Daftar_Mobil[i][2]}"
                                        del Daftar_Mobil[i] # Hapus mobil menggunakan indeks ke-(i)   
                                        print("Mobil berhasil di hapus.")                                 
                                        break

                            if not ada:
                                os.system("cls")
                                print("Mobil tidak ada dalam daftar !!!")
                                input("Tekan ENTER untuk kembali ke menu...")
                            
                            
                            

                        elif pilihan == '5':
                            os.system("cls")
                            print("Anda keluar dari Program. Sampai jumpa!")
                            Program = "n"
                            break

                        else:
                            print("Tidak ada dalam daftar")    
                            continue

    else:
        os.system("cls")
        print("="*75)
        print("Apa yang ingin anda lakukan hari ini ?")
        print("="*75)
        print("1. Daftar mobil")
        print("2. Jual Mobil") # Sama aja kayak menambahkan
        print("3. Beli Mobil") # Kalo ini, sama kayak menghapus
        print("4. Selesai")
        print("="*75)
        pilihan = input("Masukan pilihan anda (1-4) : ")

        if pilihan == "1": # tampilin daftar
            os.system("cls")
            print("="*75)
            print("Daftar Mobil di dealer Amanah")
            print("="*75)

            # Tabel
            print("=" * 75)
            print(f"{'ID':<5} | {'Merek':<10} | {'Model':<10} | {'Tahun':<6} | {'Kondisi':<7} | {'Harga (Rp.)':<20}")
            print("=" * 75)
                
            # Loop untuk daftar mobil
            for mobil in Daftar_Mobil:
                print(f"{mobil[0]:<5} | {mobil[1]:<10} | {mobil[2]:<10} | {mobil[3]:<6} | {mobil[4]:<7} | {mobil[5]:<20} ")

                print("=" * 75)
            
            input("Tekan ENTER untuk kembali ke menu...")

        elif pilihan == "2":
            os.system("cls")
            print("="*75)
            print("Mobil apa yang anda ingin jual ?")
            print("="*75)

            last_id = 0

            if Daftar_Mobil:
                for Mobil in Daftar_Mobil:
                    if Mobil[0] > last_id:
                            last_id = Mobil[0]
            id_baru = last_id + 1

            Merek = input("Masukkan Merek: ")
            Model = input("Masukkan Model: ")
            Tahun = int(input("Masukkan Tahun (Angka): ")) 
            Kondisi = input("Masukkan Kondisi (Baru/Bekas): ")
            Harga = int(input("Masukkan Harga (Angka, tanpa titik/koma): ")) 

            Mobil = [id_baru, Merek, Model, Tahun, Kondisi, Harga]
            Daftar_Mobil.append(Mobil)
            os.system("cls")
            print("Mobil anda telah berhasil dijual !")
            break

            
        elif pilihan == "3":
            os.system("cls")
            id_beli = int(input("Silahkan masukan no. mobil yang ingin anda beli (dalam bentuk angka): "))
            print("="*75)

            ada = False
        
            for i in range(len(Daftar_Mobil)):
                if Daftar_Mobil[i][0] == id_beli:
                    ada = True
                    nama_mobil = f"{Daftar_Mobil[i][1]} {Daftar_Mobil[i][2]}"
                    del Daftar_Mobil[i] # Beli mobil 
                
                    os.system("cls")
                    print("Mobil telah berhasil anda beli.")
                    Program = "n"
                    break 
                            
            if not ada: # Jika tidak ada dalam daftar
                os.system("cls")
                print("Mobil dengan ID tersebut tidak ditemukan.")
                input("Tekan ENTER untuk selesai...") 
                break

        elif pilihan == '4':
            os.system("cls")
            print("Anda keluar dari Program. Sampai jumpa!")
            Program = "n"      
            break
        
        else:
            print("Tidak ada dalam pilihan")
            break

