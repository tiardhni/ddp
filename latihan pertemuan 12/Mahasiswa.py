from Person import *
class Mahasiswa(Person):
    prodi = ""
    semester = 0

    def __init__(self, nama, umur, gender, prodi, semester):
        super().__init__(nama, umur, gender)
        self.prodi = prodi
        self.semester = semester

    def cetak(self):
        super().cetak()
        print("Prodi \t\t :", self.prodi,
              "\nSemester \t :", self.semester,
              "\n-----------------------------")