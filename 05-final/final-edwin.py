# Nama: Edwin
# NIM: D0221371
# Kelas: Informatika H

import math #utk mendapat nilai pi, digunakan dalam menghitung luas/volume tabung

#parent class
class BangunRuang:
    def luas(self):
        pass

    def volume(self):
        pass

    def printLuas(self):
        print("Luas:", self.luas())

    def printVolume(self):
        print("Volume:", self.volume())

class Balok(BangunRuang):
    def __init__(self):
        self.panjang = 0
        self.lebar = 0
        self.tinggi = 0

    def luas(self):
        l = 2 * (self.panjang * self.lebar + self.lebar * self.tinggi + self.panjang * self.tinggi)
        return l

    def volume(self):
        v = self.panjang * self.lebar * self.tinggi
        return v

class Tabung(BangunRuang):
    def __init__(self):
        self.jari_jari = 0
        self.tinggi = 0
    
    def luas(self):
        l = 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)
        return round(l, 2)
 
    def volume(self):
        v = math.pi * (self.jari_jari ** 2) * self.tinggi
        return round(v, 2)
    

class Kubus(BangunRuang):
    def __init__(self):
        self.sisi = 0

    def luas(self):
        l = 6 * (self.sisi**2)
        return l

    def volume(self):
        v = self.sisi**3
        return v

def ulang():
    print("Ingin menghitung lagi? (y/n)")
    inp = input("=> ").lower()
    return True if inp == "y" else False

#panggil class
balok = Balok()
tabung = Tabung()
kubus = Kubus()

while True:
    print("""\nPilih Bangun Ruang
1. Balok
2. Tabung
3. Kubus
4. Berhenti""")
    pilihan = input("=> ")

    if pilihan == "1":
        while True:
            print("""\n1. Luas
2. Volume
3. Keluar""")
            pilihan1 = input("=> ")
            
            if pilihan1 == "1":
                while True:
                    balok.panjang = float(input("Masukkan Panjang: "))
                    balok.lebar = float(input("Masukkan Lebar: "))
                    balok.tinggi = float(input("Masukkan Tinggi: "))

                    print()
                    balok.printLuas()

                    if ulang() != True:
                        break
            elif pilihan1 == "2":
                while True:
                    balok.panjang = float(input("Masukkan Panjang: "))
                    balok.lebar = float(input("Masukkan Lebar: "))
                    balok.tinggi = float(input("Masukkan Tinggi: "))

                    print()
                    balok.printVolume()

                    if ulang() != True:
                        break
            elif pilihan1 == "3":
                break
            else:
                print("Masukkan pilihan yang Benar!")
    elif pilihan == "2":
         while True:
            print("""\n1. Luas
2. Volume
3. Keluar""")
            pilihan2 = input("=> ")
            
            if pilihan2 == "1":
                while True:
                    tabung.jari_jari = float(input("Masukkan Jari-jari: "))
                    tabung.tinggi = float(input("Masukkan Tinggi: "))

                    print()
                    tabung.printLuas()

                    if ulang() != True:
                        break
            elif pilihan2 == "2":
                while True:
                    tabung.jari_jari = float(input("Masukkan Jari-jari: "))
                    tabung.tinggi = float(input("Masukkan Tinggi: "))

                    print()
                    tabung.printVolume()

                    if ulang() != True:
                        break
            elif pilihan2 == "3":
                break
            else:
                print("Masukkan Pilihan yang Benar!")
    elif pilihan == "3":
         while True:
            print("""\n1. Luas
2. Volume
3. Keluar""")
            pilihan3 = input("=> ")
            
            if pilihan3 == "1":
                while True:
                    kubus.sisi = float(input("Masukkan Sisi: "))

                    print()
                    kubus.printLuas()

                    if ulang() != True:
                        break
            elif pilihan3 == "2":
                while True:
                    kubus.sisi = float(input("Masukkan Sisi: "))
                    
                    print()
                    kubus.printVolume()

                    if ulang() != True:
                        break
            elif pilihan3 == "3":
                break
            else:
                print("Masukkan Pilihan yang Benar!")
    elif pilihan == "4":
        break
    else:
        print("Masukkan Pilihan yang Benar!")

print("Program berhenti. Selamat tinggal.")
