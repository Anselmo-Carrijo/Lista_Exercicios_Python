"""
Faça um Programa que leia três números e mostre o maior deles.
"""
n1 = float(input('Digite o primeiro número:\n'))
n2 = float(input('Digite o Segundo número:\n'))
n3 = float(input('Digite o Terceiro número:\n'))

if n1 <= n2 <= n3:
    print('A ordem crescente é: {},{},{}'.format(n1, n2, n3))

elif n1 <= n3 <= n2:
    print('A ordem crescente é: {},{},{}'.format(n1, n3, n2))

elif n2 <= n3 <= n1:
    print('A ordem crescente é: {},{},{}'.format(n2, n3, n1))

elif n2 <= n1 <= n3:
    print('A ordem crescente é: {},{},{}'.format(n2, n1, n3))

elif n3 <= n2 <= n1:
    print('A ordem crescente é: {},{},{}'.format(n3, n2, n1))

elif n3 <= n1 <= n2:
    print('A ordem crescente é: {},{},{}'.format(n3, n1, n2))

input()
