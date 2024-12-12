from animal import *

class Ikan(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, jenis, warna):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.jenis = jenis
        self.warna = warna
    def cetak_ikan(self):
        super().cetak() 
        print("Jenis \t\t: ", self.jenis,
        "\nWarna \t\t: ", self.warna)

nemo = Ikan("Nemo", "Plankton", "Samudra Hindia", "Bertelur", "Ikan Badut", "Oren Putih")
nemo.cetak_ikan()
print("\n")
dory = Ikan("Dory", "Tumbuhan Laut", "Laut Indonesia Timur","Bertelur", "Blue Tang", "Biru")
dory.cetak_ikan()
print("\n")
beluga = Ikan("Beluga", "Makanan laut", "Laut Arktika", "Melahirkan", "Paus", "Putih")
beluga.cetak_ikan()