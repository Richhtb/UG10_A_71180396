mahasheeshwa = input("Masukkan nama mahasiswa: ")
NIM = input("masukkan NIM-nya: ")
angkatan = NIM[2:4]
if angkatan >= "20" and angkatan <= "22":
    print(f"{mahasheeshwa} merupakan mahasiswa informatika angkatan 20 hingga 22")
else:
    print(f"{mahasheeshwa} bukan merupakan mahasiswa informatika angkatan 20 hingga 22")