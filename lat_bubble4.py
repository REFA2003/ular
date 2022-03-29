def garis():
    print("==========================")

print("HOTEL FLORIDINA")
print("TIPE KAMAR")
print("SUPERIOR, DELUXE, PREMIUM")
print("200.000, 150.000, 100.000")

tipe_kamar = input("MASUKKAN TIPE KAMAR : ")
lama_inap = int(input("LAMA INAP : "))

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

print("TIPE KAMAR : ", (tipe_kamar))
print("LAMA INAP : ", (lama_inap))
print("TOTAL HARGA : ", (total_harga))
