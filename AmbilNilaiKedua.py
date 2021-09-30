print("Hello Welcome to Mesin Penghitung Bilangan Prima")
angka1 = int(input("Dari berapa bang ? :"))
angka2 = int(input("Sampai berapa bang? :"))
angkaprima=[]

for i in range_(angka1+1, angka2+1):
    for j in range(2,i):
        if (i % j) == 0: #Kalau Genap bukan bilangan prima dong
            break
    else:
        angkaprima.append(i)
else:
    print("angka prima yang pertama adalah :", angkaprima)