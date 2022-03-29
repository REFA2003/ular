def garis():
    print("==============================")

def asc(urutan):
    urutan = sorted(urutan)
    return urutan

def desc(urutan):
    urutan = sorted(urutan, reverse = True)
    return urutan

print(" ===== MASUKKAN NILAI ===== ")

nilaiA = int(input("Masukkan Nilai A : "))
nilaiB = int(input("Masukkan Nilai B : "))
nilaiC = int(input("Masukkan Nilai C : "))
angka = [nilaiA, nilaiB, nilaiC]

garis()

def rata_rata(angka):
    return sum(angka)/len(angka)

print("URUTAN ASCENDING : ", asc(angka))
print("URUTAN DESCENDING : ", desc(angka))
print("NILAI MAX : ", max(angka))
print("NILAI MIN : ", min(angka))
print("NILAI RATA RATA : ", rata_rata(angka))


