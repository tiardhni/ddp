from animal import *

class Ular(Animal):
    def __init__(self, nama, makanan, hidup, berkembang_biak, design, racun):
        super().__init__(nama, makanan, hidup, berkembang_biak)
        self.design = design
        self.racun = racun
    def cetak_ular(self):
        super().cetak() 
        print("Design \t\t: ", self.design,
        "\nRacun \t\t: ", self.racun)

anaconda = Ular("Anaconda", "Kambing", "Amazon", "Bertelur", "Batik Solo", "Tidak Berbisa") 
anaconda.cetak_ular()
print("\n")

sanca = Ular("Sanca", "Ayam", "Sungai", "Bertelur", "Batik", "Tidak Berbisa")
sanca.cetak_ular()
print("\n")

kobra = Ular("Kobra", "Tikus", "Rawa","Bertelur", "Belang-Belang", "Berbisa")
kobra.cetak_ular()
