# Edwin
# D0221371
# Informatika H

# Python harus pakai module untuk memakai abstract class
# Abstract class adalah class yang tidak bisa dipakai
# tapi kita bisa membuat class yang "mewarisi" / inherit dari abstract class
from abc import ABC, abstractmethod
from math import pi

class BangunDatar(ABC):
    @abstractmethod
    def luas(self):
        pass

class Lingkaran(BangunDatar):
    def __init__(self, jari = 0):
        self.jari = jari

    def luas(self):
        return pi * (self.jari**2)

class Persegi(BangunDatar):
    def __init__(self, sisi = 0):
        self.__sisi = sisi

    def luas(self):
        return self.sisi * self.sisi

class Segitiga(BangunDatar):
    def __init__(self, alas = 0, tinggi = 0):
        self.alas = alas
        self.tinggi = tinggi

    def luas(self):
        return 0.5 * self.alas * self.tinggi
