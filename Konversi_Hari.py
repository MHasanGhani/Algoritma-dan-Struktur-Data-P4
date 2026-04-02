hari = int(input("Masukkan jumlah hari: "))

tahun = hari // 365
sisa = hari % 365

bulan = sisa // 30
hari_sisa = sisa % 30

print("===== HASIL KONVERSI =====")
print("Tahun :",tahun)
print("Bulan :", bulan)
print("Hari  :",hari_sisa)
