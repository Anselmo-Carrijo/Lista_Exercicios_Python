"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.

"""
import numpy
v = []

for c in range(1, 6):
    print('Informe o {}° número:'.format(c))
    n = int(input())
    v.append(n)

print('A soma é: {}'.format(sum(v)))
print('A multiplicação é: {}'.format(numpy.prod(v)))
