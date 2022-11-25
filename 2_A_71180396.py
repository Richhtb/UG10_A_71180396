print("="*5,"Selamat datang di Toko Andi Tersenyum","="*5)
TotalBelanja = int(input("Total belanja :Rp."))
if TotalBelanja < 100_000:
    print(f"tidak ada diskon ! Maka yang anda bayarkan adalah: Rp.{TotalBelanja}")
elif TotalBelanja >= 1_000_000:
    Diskon = TotalBelanja - (TotalBelanja * 0.1)
    print(f"Biaya yang harus dibayar setelah diskon adalah: Rp.{Diskon}")

elif TotalBelanja >= 500_000:
    Diskon = TotalBelanja - (TotalBelanja * 0.05)
    print(f"Biaya yang harus dibayar setelah diskon adalah: Rp.{Diskon}")

elif TotalBelanja >= 100_000 :
    Diskon= TotalBelanja - (TotalBelanja * 0.02)
    print(f"Biaya yang harus dibayar setelah diskon adalah: Rp.{Diskon}")


