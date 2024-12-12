from Mahasiswa import *
from Dosen import *
#ciptakan object
m1 = Mahasiswa('Siti Amina', 20, 'Wanita', 'SI', 3)
m2 = Mahasiswa('Rafli', 23, 'Pria', 'TI', 5)
d1 = Dosen('Sirojul Munir', 'Pria',43, 'S.Si, M.Kom', 'LPPM')
d2 = Dosen('Henry Spatono', 'Pria', 45, 'S.Si, M.Kom', 'LTSI')
#gunakan fungsi2 yang ada di class
d1.setGaji(12000000)
d2.setGaji(10000000)

m1.cetak()
m2.cetak()
d1.cetak()
d2.cetak()