nilai1 = int(input("Masukkan nilai soal 1: "))
nilai1 = nilai1 * 0.5
nilai2 = int(input("Masukkan nilai soal 2: "))
nilai2 = nilai2 * 0.3 
nilai3 = int(input("Masukkan nilai soal 3: "))
nilai3 = nilai3 * 0.2 
umur = int(input("Masukkan umur anda: "))


totalNilai = nilai1 + nilai2 + nilai3

print(f"Rata-rata nilai anda: {totalNilai}")

if totalNilai >= 80 and umur <= 25 :
    print("selamat Anda lulus!")
elif totalNilai >= 90 and umur > 25:
    print("selamat Anda lulus !") 

else: 
    print("Coba lagi tahun depan !")