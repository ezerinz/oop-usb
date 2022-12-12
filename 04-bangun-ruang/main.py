import math

class BangunRuang(object): 
    def volume(self):
        pass

    def luas(self):
        pass

    def tampilkan(self):
        print("Luas:", self.luas())
        print("Volume:", self.volume())

class Balok(BangunRuang):
    def __init__(self):
        self.panjang = 0
        self.lebar = 0
        self.tinggi = 0

    def volume(self):
        v = self.panjang * self.lebar * self.tinggi
        return v

    def luas(self):
        l = 2 * (self.panjang * self.lebar + self.lebar * self.tinggi + self.panjang * self.tinggi)
        return l

class Tabung(BangunRuang):
    def __init__(self):
        self.jari_jari = 0
        self.tinggi = 0
    
    def volume(self):
        v = math.pi * (self.jari_jari ** 2) * self.tinggi
        return v
    
    def luas(self):
        l = 2 * math.pi * self.jari_jari * (self.jari_jari + self.tinggi)
        return l

class Kubus(BangunRuang):
    def __init__(self):
        self.sisi = 0

    def volume(self):
        v = self.sisi**3
        return v

    def luas(self):
        l = 6 * (self.sisi**2)
        return l

def ulang():
    print("Ingin menghitung lagi? (y/n)")
    inp = input("=> ").lower()
    return True if inp == "y" else False
   
def hitungTabung(j, t):
    tabung.jari_jari = j
    tabung.tinggi = t

    tabung.tampilkan()

def hitungKubus(s):
    kubus.sisi = s

    kubus.tampilkan()

def hitungBalok(p, l, t):
    balok.panjang = p
    balok.lebar = l
    balok.tinggi = t

    balok.tampilkan()

#panggil objek
tabung = Tabung()
balok = Balok()
kubus = Kubus()

while True:
    print()
    print("""1. Kubus
2. Balok
3. Tabung
4. Berhenti""")
    pilihan = int(input("=> "))
    
    if pilihan == 1:
        while True:
            inp = float(input("Masukkan Sisi: "))
            hitungKubus(inp)

            if ulang() != True:
                break
    elif pilihan == 2:
        while True:
            inp = float(input("Masukkan Panjang: "))
            inp2 = float(input("Masukkan Lebar: "))
            inp3 = float(input("Masukkan Tinggi: "))
            hitungBalok(inp, inp2, inp3)

            if ulang() != True:
                break
    elif pilihan == 3:
        while True:
            inp = float(input("Masukkan Jari-jari: "))
            inp2 = float(input("Masukkan Tinggi: "))
            hitungTabung(inp, inp2)

            if ulang() != True:
                break
    elif pilihan == 4:
        break
    else:
        print("Masukkan Inputan yang Benar!")

print("Program selesai")
