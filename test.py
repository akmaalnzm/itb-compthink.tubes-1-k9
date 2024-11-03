waktu_parkir = float(input("waktu: "))
jam = int(waktu_parkir // 1)
menit = int((waktu_parkir % 1) * 60)
print(jam, menit)