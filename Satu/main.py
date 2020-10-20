
# Soal 1
print("--------------Soal 1------------------")
jml_genap = int(input("jumlah Bilangan genap : "))
n = 0;
for i in range(jml_genap):
    if i % 2 == 0:
        n += 1
print("Jumlah Bilangan genap %d" %(n))

print("-----------------------------------------------")

# Soal 2
print("--------------Soal 2------------------")
jml_genap_pertama = int(input("Jumlah bilangan genap pertama: "))

if jml_genap_pertama >= 0:
    number = 0
    i = 0
    while number <= jml_genap_pertama:
        # print(i)
        if i % 2 == 0:
            print(i)
            number += 1
            i += 1
        elif number == jml_genap_pertama:
            break
        else:
            i += 1
else:
    print("Harus lebih besar dari 0")
print("-----------------------------------------------")

print("--------------Soal 3------------------")
# Soal 3
for i in range(5):
    for j in range(5):
        if j == 2 and i == 0 or i == 4 and j == 2:
            print("0", end='')
        elif 1 <= j <= 3 and i == 1 or i == 3 and 1 <= j <= 3:
            print("0", end='')
        elif 0 <= j and i == 2:
            print("0", end='')
        else:
            print("*", end='')
    print()
print("-----------------------------------------------")