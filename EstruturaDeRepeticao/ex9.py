"""
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50

"""
for a in range(0, 50):
    if a % 2 != 0:
        print(a)

a = 0
while a < 50:
    a += 1
    if a % 2 != 0:
        print(a,'', end='')

