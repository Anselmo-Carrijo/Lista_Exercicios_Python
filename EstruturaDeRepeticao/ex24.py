"""
Faça um programa que calcule o mostre a média aritmética de N notas.

"""
n = int(input('Digite quantas notas deseja a média.\n'))
lista = []
cn = 1
for c in range(0, n):
    lista.append(int(input('Digite o primeiro {}° número.'.format(cn))))
    c += 1
    cn += 1
print('A média das {} notas fornecidas é {}.'.format(n, (sum(lista) / n)))
