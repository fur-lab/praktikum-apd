# impor os agar membersihkan layar
import os

from data import *
from greet import *
from admin import *
from pelanggan import *




### PROGRAM ###                

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
                    
                    greet_admin(Login_Username)
                    Admin = True
                    break
                    

            else:
                percobaan += 1
                print("Username atau Password salah !!!")

        while Admin == True:

            show_menu()

    else:

        os.system("cls")
        nama = input("Masukan nama anda : ")

        greet_pelanggan(nama)
        show_menu_pelanggan()


