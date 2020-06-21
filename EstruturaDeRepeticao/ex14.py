"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números impares.
"""
lista = [[], []]
valor = 0
for c in range(1, 11):
    valor = int(input(f'Digite o {c}° número. '))
    if valor % 2 != 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()

print(f'Impares são:{lista[0]}')
print(f'pares são:{lista[1]}')








