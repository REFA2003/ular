def garis():
    print("=============================")

def asc(mylist):
    mylist = sorted(mylist)
    return mylist

def desc(mylist):
    mylist = sorted(mylist, reverse = True)
    return mylist

print("Masukkan NilaiNya")

nilaiA = int(input("Masukkan Nilai A : "))
nilaiB = int(input("Masukkan Nilai B : "))
nilaiC = int(input("Masukkan Nilai C : "))
angka = [nilaiA, nilaiB, nilaiC]

garis()

def rata_rata(angka):
    return sum(angka)/len(angka)


print("Urutan Nilai Ascending  : ", asc(angka))
print("Urutan Nilai Descending : ", desc(angka))
print("Masukkan Nilai Terbesar : ", max(angka))
print("Masukkan Nilai Terkecil : ", min(angka))
print("Masukkan NIlai Rata - Rata : ", rata_rata(angka))
