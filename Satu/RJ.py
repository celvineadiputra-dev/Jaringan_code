A = int(input("genap pertama: "))

if A >= 0:
    anggka = 0
    j = 0
    while anggka <= A:
        if j % 2 == 0:
            print(j)
            anggka = anggka + 1
            j = j + 1
        elif anggka == A:
            break
        else:
            j = j + 1


for i in range(5):
    for j in range(5):
        if (j == 2 and i == 0 or i == 4 and j == 2):
            print("0", end='')
        elif (j >= 1 and j <= 3 and i == 1 or i == 3 and j >= 1 and j <= 3):
            print("0", end="")
        elif (j >= 0 and i == 2):
            print("0", end="")
        else:
            print("*", end="")
    print()




    print("----------------------------------------------")

