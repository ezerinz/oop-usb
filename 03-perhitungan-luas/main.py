# Nama  : Edwin
# NIM   : D0221371
# Kelas : Informatika H

import bangundatar as bd

lingkaran = bd.Lingkaran()
segitiga = bd.Segitiga()
persegi = bd.Persegi()
luas = 0

while True:
    print()
    print("""1. Hitung Luas Segitiga
2. Hitung Luas Persegi
3. Hitung Luas Lingkaran
4. Berhenti""")
    pilihan = int(input("=> "))

    if pilihan == 1:
        segitiga.alas = float(input("Masukkan Alas: "))
        segitiga.tinggi = float(input("Masukkan Tinggi: "))
        luas = segitiga.luas()
    elif pilihan == 2:
        persegi.sisi = float(input("Masukkan Sisi: "))
        luas = persegi.luas()
    elif pilihan == 3:
        lingkaran.jari = float(input("Masukkan Jari-jari: "))
        luas = lingkaran.luas()
    elif pilihan == 4:
        break
    else:
        print("Periksa Kembali Inputan!")
    
    print("Luas: ", luas)

print("Selamat Tinggal")
