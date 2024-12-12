from animal import *

class Burung(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, bunyi):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.bunyi = bunyi
    def cetak_burung(self):
        super().cetak() 
        print("Jenis \t\t: ", self.jenis,
        "\nBunyi \t\t: ", self.bunyi)


Gereja = Burung("Gereja", "Biji", "Taman", "Bertelur", "Burung Hantu", "Tweeee")
Gereja.cetak_burung()
print("\n")
kutilang = Burung("Kutilang", "cacing", "kebun", "Bertelur", "Pengicau", "pipipippp")
kutilang.cetak_burung()
print("\n")
merpati = Burung("Merpati", "Sayuran", "Rumah", "Bertelur", "Merpati Homer", "ccicuitt")
merpati.cetak_burung()