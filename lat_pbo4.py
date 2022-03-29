def garis():
    print("=========================")

def asc(mylist):
    mylist = sorted(mylist)
    return mylist

def desc(mylist):
    mylist = sorted(mylist, reverse = True)
    return mylist

print("MASUKKAN NILAI")

nilaiA = int(input("Masukkan Nilai A : "))
nilaiB = int(input("Masukkan Nilai B : "))
nilaiC = int(input("Masukkan Nilai C : "))

angka = [nilaiA, nilaiB, nilaiC]

def rata_rata(angka):
    return sum(angka)/len(angka)

print("Ascending : ", asc(angka))
print("Descending : ", desc(angka))
print("MAX : ", max(angka))
print("MIN : ", min(angka))
print("Rata - Rata : ", rata_rata(angka))

home = input("Kembali Ke Menu Utama (Y/N) ? ")
text = print("Progam Mengurutkan Data menggunaka metode Bubble sort")
back = print("")
garis()

if home == "Y":
    def asc(mylist):
        mylist = sorted(mylist)
        return mylist

    def desc(mylist):
        mylist = sorted(mylist, reverse = True)
        return mylist

    print("MASUKKAN NILAI")
    nilaiA = int(input("Masukkan Nilai A : "))
    nilaiB = int(input("Masukkan Nilai B : "))
    nilaiC = int(input("Masukkan Nilai C : "))

    angka = [nilaiA, nilaiB, nilaiC]

    def rata_rata(angka):
        return sum(angka)/len(angka)

    print("Ascending : ", asc(angka))
    print("Descending : ", desc(angka))
    print("MAX : ", max(angka))
    print("MIN : ", min(angka))
    print("Rata - Rata : ", rata_rata(angka))
else:
    back
