# Bulit in dan func library

# x = 42
# def fungsi():
#     x = 10
#     y = 20
#     z = 30
#     print(globals()['x']) # mendapatkan isi dari variabel x (global)
#     print(locals()['x']) # mendapatkan isi dari variabel x (lokal)
#     print(locals()) # {'x': 10, 'y': 20, 'z': 30}
# fungsi()

# nama = input("Masukan nama kalian : ")
# print(nama.lower()) # huruf kecil semua
# print(nama.upper()) # huruf kapital semua

# import random
# print(random.randint(1, 5)) # menghasilkan angka random dari 1 - 4
# pilih_acak = ["pisang", "rambutan", "manggis"]
# acak = "apcb"
# print(random.choice(pilih_acak)) # memilih 1 element secara acak pada list
# print(random.choice(acak)) # memilih 1 karakter acak pada string
# # memasukkan satu persatu nilai dari kumpulan_angka
# # ke dalam variabel hasil dengan isinya 4 karakter hasil randomize
# kumpulan_angka = "1234567890"
# hasil = ""
# for i in range(4):
#     hasil += random.choice(kumpulan_angka)
#     print(hasil)

# acak_kartu = ["1 wajik", "3 wajik", "5 wajik"]
# random.shuffle(acak_kartu) # kocok kartu, output berupa urutan list yang berubah
# print(acak_kartu)
# # random = pilih satu
# # shuffle = acak urutan


# prettytable, atau bisa pakai taboilate?
# bikin tabel
# from prettytable import PrettyTable
# table = PrettyTable()

# table.field_names = ["ID", "Nama", "Prodi", "NIM"]
# table.add_row(["001", "Rafli", "Infor", "013"])
# table.add_row(["002", "Putra", "Infor", "013"])
# table.add_row(["003", "Risdi", "Infor", "013"])

# print(table)
# print(table.get_string())



# import inquirer
# pertanyaan = [
#     inquirer.List( # bikin list
#     'size',
#     message="What size do you need?", # sama kyk print
#     choices=['Jumbo', 'Large', 'Standard', 'Medium', 'Small', 'Micro'], # pilihannya
#     ),
# ]
# # mendapatkan jawaban
# answer = inquirer.prompt(pertanyaan)
# print(answer) # Output dalam bentuk Dictionary {'size': 'Large'}
# print(answer['size']) # Ambil value dari key 'size' (Large)

# # cara bikin arrow