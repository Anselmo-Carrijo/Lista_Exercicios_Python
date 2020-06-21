"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
A: o produto do dobro do primeiro com metade do segundo .
B: a soma do triplo do primeiro com o terceiro.
C: o terceiro elevado ao cubo.

"""
n1 = int(input('Digite um número inteiro: '))
n2 = int(input('Digite outro número inteiro:'))
n3 = float(input('Digite um número real:'))

a = (n1 * 2) * (n2 / 2)
b = (n1 * 3) + n3
c = n3 ** 3

print('O produto do dobro do primeiro com metade do segundo é {},A soma do triplo do primeiro'
      '\ncom o terceiro é {} e o terceiro elevado ao cubo é {} '.format(a, b, c))
