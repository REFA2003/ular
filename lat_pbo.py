def garis():
    print("================================")

def asc(mylist):
    mylist = sorted(mylist)
    return mylist

def desc(mylist):
    mylist = sorted(mylist, reverse = True)
    return mylist

print("Masukkan Nilai")

nilaiA = int(input("Masukkan Nilai A : "))
nilaiB = int(input("Masukkan Nilai B : "))
nilaiC = int(input("Masukkan Nilai C : "))
angka = [nilaiA, nilaiB, nilaiC]

garis()

def rata_rata(angka):
    return sum(angka)/len(angka)

print("Urutan nilai Ascending : ")
print(asc(angka))

print("Urutan nilai Descending : ")
print(desc(angka))

print("Nilai Terbesar : ", max(angka))
print("Nilai Terkecil : ", min(angka))
print("Nilai Rata - Rata : ", rata_rata(angka))
