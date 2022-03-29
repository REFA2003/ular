def garis():
    print("===========================")

print("===== HOTEL PARAGON =====")
print("===== TIPE KAMAR =====")
print("--- superior -- deluxe -- premium ---")
print("-- 200.000/day - 150.000/day - 150.000/day --")

tipe_kamar = input("Masukkan Tipe Kamar : ")
lama_inap = int(input("Lama Penginapan : "))

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

print("Tipe kamar Yang Di Pilih : ", (tipe_kamar))
print("Lama Penginapan : ", (lama_inap))
print("Total Harga Yang Di Bayarkan : ", (total_harga))
