import os
os.system("clear")

n1 = int(input('Digite um numero: '))
n2 = int(input('Digite um numero: '))
    cont = 0
    for j in range(1, n2):
        if c % j == 0:
            cont += 1
        if c == 2:
            cont += 1
    if cont == 2:
        print(c, end=' ')
