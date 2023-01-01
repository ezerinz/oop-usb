# Nama: Edwin
# NIM: D0221371
# Kelas: Informatika H

from math import pi #utk mendapat nilai pi, digunakan dalam menghitung luas/volume tabung

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
        self.panjang = float(input("Masukkan Panjang: "))
        self.lebar = float(input("Masukkan Lebar: "))
        self.tinggi = float(input("Masukkan Tinggi: "))

    def luas(self):
        l = 2 * (self.panjang * self.lebar + self.lebar * self.tinggi + self.panjang * self.tinggi)
        return l

    def volume(self):
        v = self.panjang * self.lebar * self.tinggi
        return v

class Tabung(BangunRuang):
    def __init__(self):
        self.jari_jari = float(input("Masukkan Jari-jari: "))
        self.tinggi = float(input("Masukkan Tinggi: "))
    
    def luas(self):
        l = 2 * pi * self.jari_jari * (self.jari_jari + self.tinggi)
        return round(l, 2)
 
    def volume(self):
        v = pi * (self.jari_jari ** 2) * self.tinggi
        return round(v, 2)
    

class Kubus(BangunRuang):
    def __init__(self):
        self.sisi = float(input("Masukkan Sisi: "))

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

while True:
    print("""\nPilih Bangun Ruang
1. Balok
2. Tabung
3. Kubus
4. Berhenti""")
    pilihan = input("=> ")

    if pilihan == "1":
        while True:
            balok = Balok()
            
            print("""\n1. Luas
2. Volume
3. Keluar""")
            pilihan1 = input("=> ")
            print()

            if pilihan1 == "1":
                balok.printLuas()
            elif pilihan1 == "2":
                balok.printVolume()
            elif pilihan1 == "3":
                break
            else:
                print("Masukkan pilihan yang Benar!")

            if ulang() != True:
                break
    elif pilihan == "2":
         while True:
            tabung = Tabung()

            print("""\n1. Luas
2. Volume
3. Keluar""")
            pilihan2 = input("=> ")
            print()

            if pilihan2 == "1":
                tabung.printLuas()
            elif pilihan2 == "2":
                tabung.printVolume()
            elif pilihan2 == "3":
                break
            else:
                print("Masukkan Pilihan yang Benar!")

            if ulang() != True:
                break
    elif pilihan == "3":
         while True:
            kubus = Kubus()

            print("""\n1. Luas
2. Volume
3. Keluar""")
            pilihan3 = input("=> ")
            print()

            if pilihan3 == "1":
                kubus.printLuas()
            elif pilihan3 == "2":
                kubus.printVolume()
            elif pilihan3 == "3":
                break
            else:
                print("Masukkan Pilihan yang Benar!")

            if ulang() != True:
                break
    elif pilihan == "4":
        break
    else:
        print("Masukkan Pilihan yang Benar!")

print("Program berhenti. Selamat tinggal.")
