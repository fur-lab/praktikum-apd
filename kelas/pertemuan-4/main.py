# for
# ulangi = 10
# for i in range (ulangi):
#     print(f"Perulangan ke {i}")

# # list
# simpan = [1, 'Dapupu', 4.00, True]
# for i in simpan:
#     print(i)            # ini sampai list simpan indeks terakhir

# # Nested for (looping di dalam looping)
# for i in range(1, 4):# Mengontrol baris dalam tabel perkalian
#     for j in range(1, 5):# Mengontrol kolom dalam tabel perkalian
#         print(f'{i} x {j} = {i * j}')
#     print('') #biar ada jarak tiap iterasi

# # while
# jawab = 'ya'
# hitung = 0
# while(jawab == 'ya'):
#     hitung += 1
#     jawab = input("Ulang lagi? ")
#     print(f"Total perulangan: {hitung}")

# # segitiga siku-siku
# for i in range (1, 10):
#     print("#"* i)

# break
# angka = [2, 5, 8, 9, 15, 7, 20]
# print("Mencari angka pertama yang lebih besar dari 10...")

# for i in angka:
#     print(f"Sekarang memeriksa angka: {i}")

#     if i > 10:
#         print(f"Angka {i} lebih besar dari 10, Perulangan berhenti.")
#         break
# print("Program selesai.")

# # continue
# for i in range(1, 11):
#     if i % 2 == 0:
#         continue
#     print(f"Angka genap ditemukan: {i}")
# print("\nProgram selesai.")

# frre post test
h = 5
for i in range (1, h):
    hkiri = "*" * i
    tes = "x"*((h-i)*2)
    hkanan = "*" * i
    print(hkiri + tes + hkanan)