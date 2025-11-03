import os

from admin import *
from prettytable import PrettyTable


def show_menu_pelanggan():
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
            Menu()


        elif pilihan == "2":
            Jual()

            
        elif pilihan == "3":
            Beli()                     

        elif pilihan == '4':
            Exit()
        
        else:
            os.system("cls")
            print("Tidak ada dalam daftar") 
            input("Tekan ENTER untuk mulai ulang...")
    
def Jual():
            os.system("cls")
            print("="*75)
            print("Mobil apa yang anda ingin jual ?")
            print("="*75)

            last_id = 0

            for Mobil in Daftar_Mobil:
                if Mobil > last_id:
                    last_id = Mobil
            id_baru = last_id + 1

            try:
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

            except ValueError:
                print("Tahun dan Harga harus angka !")
                input("Tekan ENTER untuk kembali ke menu...")
                return
            
            os.system("cls")
            print("Mobil anda telah berhasil dijual !")
            input("Tekan ENTER untuk mulai ulang...")

def Beli():
        os.system("cls")

        try:
            id_beli = int(input("Silahkan masukan no. mobil yang ingin anda beli (dalam bentuk angka): "))

        except ValueError:
            print("Harus angka !")
            input("Tekan ENTER untuk kembali ke menu...")
            return
        
        print("="*75)

        if id_beli in Daftar_Mobil:
                    
                    del Daftar_Mobil[id_beli]   
                    print("Mobil berhasil di beli.")                                 
        input("Tekan ENTER untuk kembali ke menu...")
        