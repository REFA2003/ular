def garis():
    print("===============================")

print("========== HOTEL OYO =========")
print("----- superior ----- deluxe ----- premium -----")
print("----- 200000/day --- 150000/day --- 100000/day -----")
garis()

tipe_kamar = input("Masukkan Tipe Kamar : ")
lama_inap = int(input("Lama Inap : "))

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
print("Lama Inap : ", (lama_inap))
print("Total Harga : ", (total_harga))

home = input("Kembali Ke menu utama Y/N")
back = print()

garis()

if home == "Y":

    tipe_kamar = input("Masukkan Tipe Kamar : ")
    lama_inap = int(input("Lama Inap : "))

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
else:
    back
