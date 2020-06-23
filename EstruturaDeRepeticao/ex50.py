"""
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, Faça um programa que calcule o valor de H com N termos.

"""

n = int(input('Informe o número n:\n'))
numerador = 1
denominador = 0
h = 0
for i in range(n):
    print('Termo {}: {}/{}'.format(i + 1, numerador, denominador + 1))
    denominador += 1
    h += (numerador / denominador)
print('A soma é {:.2f}'.format(h))