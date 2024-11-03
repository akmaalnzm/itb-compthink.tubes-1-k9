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

# KAMUS


# [1] Identifikasi pengguna
verifikasi = False
while verifikasi == False:
    while True:
        jenis_kendaraan = input("Apa jenis kendaraan anda? (Mobil/Motor) ").strip().lower()
        if jenis_kendaraan == "mobil" or jenis_kendaraan == "motor":
            # print(f"Jenis kendaraan anda adalah {jenis_kendaraan}")
            break
        else: 
            print("Jenis kendaraan tidak diketahui.")

    while True:
        status_member = input("Apakah anda member? (y/n) ").strip().lower()
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
            saldo_emoney = int(input("Masukkan saldo e-money: (Rupiah) "))
            # print(f"Saldo anda: Rp{saldo_emoney},00")
            break
        except ValueError:
            print("Masukkan nominal dalam angka (Rupiah)")

    print("====== Data Anda ======")
    print("Jenis Kendaraan:", jenis_kendaraan)
    print("Status Member:", status_member )
    print(f"Saldo e-money: Rp{saldo_emoney}")
    print("=======================")

    while True:
        konfirmasi = input("Apakah anda member? (y/n) ").strip().lower()
        if konfirmasi == "y" or konfirmasi == "n":
            break
    if konfirmasi == "y":
        verifikasi = True
    else: 
        print("Perbaiki data: ")




#### Program Utama
# [2] Penampilan layar parking gate (masuk)

# [3] Perhitungan tarif parkir

# [4] Penampilan layar parking gate (keluar)
####

# [5] Pengisian ulang saldo


# Program simulasi

