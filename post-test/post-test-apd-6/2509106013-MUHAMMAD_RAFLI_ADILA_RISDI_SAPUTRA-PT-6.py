# impor os agar membersihkan layar
import os

# username, password dan status admin buat masuk ke menu admin
Username = "Rafli"
Password = "013"
Admin = False

# Logika buat Program berlanjut
Program ="y"

# daftar
Daftar_Mobil = {
1 : {"Merek" : "Toyota", "Model" : "Yaris", "Tahun" : 2011, "Kondisi" : "Bekas", "Harga" : 130000000},
2 : {"Merek" : "Honda", "Model" : "City", "Tahun" : 2005, "Kondisi" : "Bekas", "Harga" : 70000000},
3 : {"Merek" : "Daihatsu", "Model" : "Ayla", "Tahun" : 2011, "Kondisi" : "Baru", "Harga" : 160000000}
}

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

                            for Mobil in Daftar_Mobil: # perulangan untuk id mobil agar tidak ada yang sama
                                if Mobil > last_id:
                                    last_id = Mobil
                            id_baru = last_id + 1

                            Merek = input("Masukkan Merek: ")
                            Model = input("Masukkan Model: ")
                            Tahun = int(input("Masukkan Tahun (Angka): ")) 
                            Kondisi = input("Masukkan Kondisi (Baru/Bekas): ")
                            Harga = int(input("Masukkan Harga (Angka, tanpa titik/koma): ")) 

                            Daftar_Mobil[id_baru] = { # menambahkan dengan key ID = "id_baru" dan value merek,dll
                                "Merek": Merek,
                                "Model": Model,
                                "Tahun": Tahun,
                                "Kondisi": Kondisi,
                                "Harga": Harga
                            }
                            
                        elif pilihan == "2": # Read
                            os.system("cls")
                            print("="*75)
                            print("Daftar Mobil di dealer Amanah")
                            print("="*75)

                            # Tabel
                            print("=" * 75)
                            print(f"{"ID":<5} | {"Merek":<10} | {"Model":<10} | {"Tahun":<6} | {"Kondisi":<7} | {"Harga (Rp.)":<20}")
                            print("=" * 75)
                                
                            # Loop untuk daftar mobil
                            for Mobil, detail_mobil in Daftar_Mobil.items():
                                Merek = detail_mobil["Merek"]
                                Model = detail_mobil["Model"]
                                Tahun = detail_mobil["Tahun"]
                                Kondisi = detail_mobil["Kondisi"]
                                Harga = detail_mobil["Harga"]

                                print(f"{Mobil:<5} | {Merek:<10} | {Model:<10} | {Tahun:<6} | {Kondisi:<7} | {Harga:<20}")

                                print("=" * 75)
                            
                            input("Tekan ENTER untuk kembali ke menu...")

                        elif pilihan == "3": # Update
                            os.system("cls")
                            id_Ubah = int(input("Masukan ID Mobil yang ingin anda ubah (dalam bentuk angka): "))

                            for Mobil, detail_mobil in Daftar_Mobil.items():

                                if id_Ubah in Daftar_Mobil:
                                    detail_mobil = Daftar_Mobil[id_Ubah]
                                    print(f"Anda akan mengubah {detail_mobil["Merek"]} ? ")

                                    harga_baru_edit = int(input("Masukan Harga (angka saja): "))
                                    Daftar_Mobil[id_Ubah]["Harga"] = harga_baru_edit

                                    os.system("cls")
                                    print("Harga mobil telah berhasil diubah")

                                    break 
            
                            input("Tekan ENTER untuk kembali ke menu...")

                        elif pilihan == "4": # Delete
                            os.system("cls")

                            id_hapus = int(input("Silahkan masukan no. mobil yang ingin anda hapus (dalam bentuk angka): "))
                        
                            if id_hapus in Daftar_Mobil:
                                
                                del Daftar_Mobil[id_hapus]   
                                print("Mobil berhasil di hapus.")     
                                                            
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
            # Loop untuk daftar mobil
            for Mobil, detail_mobil in Daftar_Mobil.items():
                Merek = detail_mobil["Merek"]
                Model = detail_mobil["Model"]
                Tahun = detail_mobil["Tahun"]
                Kondisi = detail_mobil["Kondisi"]
                Harga = detail_mobil["Harga"]

                print(f"{Mobil:<5} | {Merek:<10} | {Model:<10} | {Tahun:<6} | {Kondisi:<7} | {Harga:<20}")

                print("=" * 75)
            
            input("Tekan ENTER untuk kembali ke menu...")

        elif pilihan == "2":
            os.system("cls")
            print("="*75)
            print("Mobil apa yang anda ingin jual ?")
            print("="*75)

            last_id = 0

            for Mobil in Daftar_Mobil:
                if Mobil > last_id:
                    last_id = Mobil
            id_baru = last_id + 1

            Merek = input("Masukkan Merek: ")
            Model = input("Masukkan Model: ")
            Tahun = int(input("Masukkan Tahun (Angka): ")) 
            Kondisi = input("Masukkan Kondisi (Baru/Bekas): ")
            Harga = int(input("Masukkan Harga (Angka, tanpa titik/koma): ")) 

            Daftar_Mobil[id_baru] = {
                "Merek": Merek,
                "Model": Model,
                "Tahun": Tahun,
                "Kondisi": Kondisi,
                "Harga": Harga
            }
            os.system("cls")
            print("Mobil anda telah berhasil dijual !")
            break

            
        elif pilihan == "3":
            os.system("cls")
            id_beli = int(input("Silahkan masukan no. mobil yang ingin anda beli (dalam bentuk angka): "))
            print("="*75)

            if id_beli in Daftar_Mobil:
                        
                        del Daftar_Mobil[id_beli]   
                        print("Mobil berhasil di beli.")                                 
            input("Tekan ENTER untuk kembali ke menu...")
                            

        elif pilihan == '4':
            os.system("cls")
            print("Anda keluar dari Program. Sampai jumpa!")
            Program = "n"      
            break
        
        else:
            print("Tidak ada dalam pilihan")
            break

