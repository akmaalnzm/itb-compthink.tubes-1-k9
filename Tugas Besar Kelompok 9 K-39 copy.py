# TUGAS BESAR PENGENALAN KOMPUTASI K-39
# "Automatic Parking Gate"

# Kelompok 9 K-39
#   Muhammad Abrar Adhyatama        (16924163)
#   Aldy Nahri Rafansyah            (16924165)
#   Aditya Rianda Subarkah          (16924168)
#   Julius Kevin Saputra            (16924169)
#   Akmal Nizam Aminudin            (16924177)
#   Reynaldi Putra Langit           (16924178)


# Deskripsi : Program simulasi sistem parkir otomatis dengan metode pembayaran non tunai


# [1] Inisialisasi data user

print("============== Pengisian Data ==================")
verifikasi = False
while verifikasi == False:
    while True:
        jenis_kendaraan = input("> Apa jenis kendaraan anda? (Mobil/Motor) ").strip().lower()
        if jenis_kendaraan == "mobil" or jenis_kendaraan == "motor":
            # print(f"Jenis kendaraan anda adalah {jenis_kendaraan}")
            break
        else: 
            print("Jenis kendaraan tidak diketahui.")

    while True:
        status_member = input("> Apakah anda member? (y/n) ").strip().lower()
        if status_member == "y":
            status_member = True
            # print("Anda adalah member")
            break
        elif status_member == "n":
            status_member = False
            # print("Anda bukan member")
            break
        else:
            print("Pastikan anda member atau bukan.")

    while True:
        try: 
            saldo_emoney = int(input("> Masukkan saldo e-money: (Rupiah) "))
            # print(f"Saldo anda: Rp{saldo_emoney},00")
            break
        except ValueError:
            print("Masukkan nominal dalam angka (Rupiah)")
    
    print()
    print("================= Data Anda ====================")
    print("Jenis Kendaraan  :", jenis_kendaraan)
    print("Status Member    :", status_member )
    print(f"Saldo e-money    : Rp{saldo_emoney}")
    print("================================================")
    print()

    while True:
        konfirmasi = input("> Mulai simulasi? (y/n) ").strip().lower()
        if konfirmasi == "y" or konfirmasi == "n":
            break
    if konfirmasi == "y":
        verifikasi = True
        print()
    else: 
        print("Perbaiki data: ")


# [2] Penampilan layar parking gate (masuk)

print("================================================")
print("               Selamat Datang!                  ")
print("     Silahkan Tap Kartu Member atau E-money     ")
print("================================================")
print("                Tarif Parkir:                   ")
print("      Waktu      ||    Mobil    ||    Motor    || ")
print("  1 Jam Pertama  ||    Rp5000   ||    Rp3000   || ")
print(" /Jam Berikutnya ||    Rp3000   ||    Rp2000   || ")
print("================================================")
print()

while True: 
    metode_masuk = input("> Metode masuk: (member/emoney) ").strip().lower()
    if metode_masuk == "member":
        if status_member == True:
            break
        else: 
            print("Anda tidak terdaftar sebagai member.")
    elif metode_masuk == "emoney":
        break
    else:
        print("Metode masuk tidak diketahui.")

print()
print("================================================")
print("                 Gate Terbuka                   ")
print("                Silahkan Masuk                  ")
print("================================================")
print("Jenis Kendaraan  :", jenis_kendaraan)
print("Metode masuk     :", metode_masuk)
print("================================================")
print()

# [3] Penentuan tarif parkir & pembayaran

while True:
    try: 
        waktu_parkir = float(input("> Lama waktu parkir (dalam jam): "))
        break
    except ValueError: 
        print("Masukkan lama waktu parkir dalam jam")


# Tarif mobil
if jenis_kendaraan == "mobil":
    if waktu_parkir == 1:
        tarif_parkir = 5000
    if waktu_parkir > 1:
        tarif_parkir = 5000 + ((waktu_parkir // 1) - 1)*3000

# Tarif motor
if jenis_kendaraan == "motor":
    if waktu_parkir == 1:
        tarif_parkir = 3000
    if waktu_parkir > 1:
        tarif_parkir = 3000 + ((waktu_parkir // 1) - 1)*2000

# formatting waktu parkir
jam = int(waktu_parkir // 1)
menit = int((waktu_parkir % 1 * 60))

if metode_masuk == "member":
    print()
    print("================================================")
    print("                 Gate Terbuka                  ")
    print("                 Selamat Jalan                  ")
    print("================================================")
    print("Waktu parkir     :", f"{jam} jam {menit} menit")
    print("Jenis Kendaraan  :", jenis_kendaraan)
    print("Metode masuk     :", metode_masuk)
    print("Tarif Pakir      : Rp0,00")
    print("================================================")
else: 
    print()
    print("================================================")
    print("                 Gate Tertutup                  ")
    print("================================================")
    print("Waktu parkir     :", f"{jam} jam {menit} menit")
    print("Jenis Kendaraan  :", jenis_kendaraan)
    print("Metode masuk     :", metode_masuk)
    print("Tarif Pakir      :", f"Rp{int(tarif_parkir)},00")
    print("================================================")
    print()

    while True:
        tap = input("> Tap emoney? (y/n) ").strip().lower()
        if tap == "y":
            break
        elif tap == "n":
            print("Tap emoney untuk keluar.")
    if tap == "y":
        while saldo_emoney < tarif_parkir:
            # pengisian ulang saldo
            print("Saldo anda tidak cukup. Silahkan isi ulang saldo.")
            saldo_emoney = saldo_emoney + int(input("Isi ulang saldo sebesar: "))
            print(f"Saldo anda sekarang: Rp{saldo_emoney},00")
        print()
        print("================================================")
        print("                 Gate Terbuka                  ")
        print("                 Selamat Jalan                  ")
        print("================================================")
        print("Waktu parkir     :", f"{jam} jam {menit} menit")
        print("Jenis Kendaraan  :", jenis_kendaraan)
        print("Metode masuk     :", metode_masuk)
        print("Tarif Pakir      :", f"Rp{int(tarif_parkir)},00")
        print("Sisa saldo       :", f"Rp{int(saldo_emoney - tarif_parkir)},00")
        print("================================================")

