#buka file txt 
file = "data.txt"
data = open(file, "r")
baris = data.readlines()
pin = int(baris[0].strip())

def simpankeData(baru):
    ganti = open(file, "w")
    ganti.writelines(baru)
    ganti.close

def ganti_pin(pinBaru):
    baris[0] = pinBaru+"\n"
    simpankeData(baris)
    print("Pin terganti.")

def tarikTunai(jumlahTarik, saldo):
    if jumlahTarik > saldo:
        print("Saldo Anda tidak cukup")
    else:
        print(f"Sebanyak Rp{jumlahTarik} ditarik.")
        sisa = saldo - jumlahTarik
        print(f"Sisa saldo Anda: Rp{sisa}")
        baris[1] = str(sisa)+"\n" 
        simpankeData(baris)

def setorTunai(jumlahSetor, saldo):
    print(f"Sebanyak Rp{jumlahSetor} disetor.")
    total = saldo + jumlahSetor
    print(f"Sisa saldo Anda: Rp{total}")
    baris[1] = str(total)+"\n"
    simpankeData(baris)

def infoSaldo(saldo):
    print(f"Sisa Saldo: Rp{saldo}")

def stop():
    print()
    print("""Selesai!
Hentikan program? (y/n)""")
    return input("=> ").lower()

inPin = int(input("Masukkan Pin: "))
while inPin == pin:
    saldoo = int(baris[1].strip())
    print()
    print("Selamat Datang!")
    print("""1. Cek Saldo
2. Tarik Tunai
3. Setor Tunai         
4. Ganti Pin
5. Berhenti""")
    pilihan = int(input("=> "))

    if pilihan == 1:
        print()
        infoSaldo(saldoo)
        if stop() == "y":
            break
    elif pilihan == 2:
        print()
        jumlah = int(input("Jumlah tarik tunai: Rp"))
        tarikTunai(jumlah, saldoo)
        if stop() == "y":
            break
    elif pilihan == 3:
        print()
        jumlah = int(input("Jumlah setoran: Rp"))
        setorTunai(jumlah, saldoo)

        if stop() == "y":
            break
    elif pilihan == 4:
        print()
        newPin = input("Masukkan Pin Baru: ")
        if len(newPin) > 6:
            print("Karakter maksimal untuk Pin adalah enam!")
        else:
            ganti_pin(newPin)
        if stop() == "y":
            break
    elif pilihan == 5:
        break
    else:
        print()
        print("Periksa inputan dengan benar!")

else:
    print("Pin Anda salah, program akan berhenti!")
