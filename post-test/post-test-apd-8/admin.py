import os

from data import *
from prettytable import PrettyTable

def show_menu():

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
        Tambah_mobil()
    elif pilihan == "2": # Read
        Menu()
    elif pilihan == "3": # Update
        Update()
    elif pilihan == "4": # Delete
        Delete()
    elif pilihan == '5':
        Exit()    
    else:
        os.system("cls")
        print("Tidak ada dalam daftar") 
        input("Tekan ENTER untuk lanjut ke menu admin...")

def Tambah_mobil():
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

        try :
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
        except ValueError:
            print("Tahun dan Harga harus angka !")
            input("Tekan ENTER untuk kembali ke menu...")
            return

def Menu():
    os.system("cls")
    print("="*75)
    print("Daftar Mobil di dealer Amanah")
    print("="*75)

    # Tabel
    table = PrettyTable()
    table.field_names = ["ID", "Merek", "Model", "Tahun", "Kondisi", "Harga"]
    
    # Loop untuk daftar mobil
    for Mobil, detail_mobil in Daftar_Mobil.items():
        table.add_row([Mobil, detail_mobil["Merek"], detail_mobil["Model"], detail_mobil["Tahun"], detail_mobil["Kondisi"], detail_mobil["Harga"]])
    print(table)

    input("Tekan ENTER untuk kembali ke menu...")

def Update():
    os.system("cls")
    try :
        id_Ubah = int(input("Masukan ID Mobil yang ingin anda ubah (dalam bentuk angka): "))
    
    except ValueError:
            print("Harus angka !")
            input("Tekan ENTER untuk kembali ke menu...")
            return

    if id_Ubah in Daftar_Mobil:
        detail_mobil = Daftar_Mobil[id_Ubah]
        print(f"Anda akan mengubah {detail_mobil["Merek"]} ? ")

        try : 
            harga_baru_edit = int(input("Masukan Harga (angka saja): "))

        except ValueError:
            print("Harga harus angka !")
            input("Tekan ENTER untuk kembali ke menu...")
            return
        
        Daftar_Mobil[id_Ubah]["Harga"] = harga_baru_edit

        os.system("cls")
        print("Harga mobil telah berhasil diubah")

    input("Tekan ENTER untuk kembali ke menu...")

def Delete():
    os.system("cls")

    try:
        id_hapus = int(input("Silahkan masukan no. mobil yang ingin anda hapus (dalam bentuk angka): "))
    
    except ValueError:
            print("Harus angka !")
            input("Tekan ENTER untuk kembali ke menu...")
            return

    if id_hapus in Daftar_Mobil:
        
        del Daftar_Mobil[id_hapus]   
        print("Mobil berhasil di hapus.")     
    
    input("Tekan ENTER untuk kembali ke menu...")

def Exit():

    global Admin
    global Program

    os.system("cls")
    print("Anda keluar dari Program. Sampai jumpa!")
    Program = "n"
    Admin = False