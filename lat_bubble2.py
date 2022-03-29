def garis():
    print("============================")

print("========== HOTEL DUBAI ==========")
print("========== TIPE KAMAR ==========")
print("--- superior -- deluxe -- premium ---")
print("-- 200.000/day - 150.000/day - 100.000/day --")

tipe_kamar = input("Masukkan Tipe Kamar : ")
lama_inap = int(input("Lama Waktu Inap : "))

if tipe_kamar == "superior":
    if lama_inap <= 2:
        total_harga = 200000*lama_inap
    elif lama_inap <= 4:
        total_harga = 200000*lama_inap
    else:
        total_harga = 600000

if tipe_kamar == "deluxe":
    if lama_inap <= 2:
        total_harga = 150000*lama_inap
    elif lama_inap <= 4:
        total_harga = 150000*lama_inap
    else:
        total_harga = 150000*lama_inap

if tipe_kamar == "premium":
    if lama_inap <= 2:
        total_harga = 100000*lama_inap
    elif lama_inap <= 4:
        total_harga = 100000*lama_inap
    else:
        total_harga = 100000*lama_inap

garis()

print("Tipe Kamar Yang Dipilih : ", (tipe_kamar))
print("Lama Waktu Inap : ", (lama_inap))
print("Total Harga : ", (total_harga))

home = input("Kembali Memesan (Y//N)")
back = print("")

garis()

if home == "Y":
    tipe_kamar = input("Masukkan Tipe Kamar : ")
    lama_inap = int(input("Lama Waktu Inap : "))

    if tipe_kamar == "superior":
        if lama_inap <= 2:
            total_harga = 200000*lama_inap
        elif lama_inap <= 4:
            total_harga = 200000*lama_inap
        else:
            total_harga = 600000

    if tipe_kamar == "deluxe":
        if lama_inap <= 2:
            total_harga = 150000*lama_inap
        elif lama_inap <= 4:
            total_harga = 150000*lama_inap
        else:
            total_harga = 150000*lama_inap

    if tipe_kamar == "premium":
        if lama_inap <= 2:
            total_harga = 100000*lama_inap
        elif lama_inap <= 4:
            total_harga = 100000*lama_inap
        else:
            total_harga = 100000*lama_inap
    garis()

    print("Tipe Kamar Yang Dipilih : ", (tipe_kamar))
    print("Lama Waktu Inap : ", (lama_inap))
    print("Total Harga : ", (total_harga))
else:
    back
