"""
Faça um Programa que peça dois números e imprima o maior deles.

"""

n1 = float(input('Digite um número qualquer:\n'))
n2 = float(input('Digite um outro número qualquer:\n'))

if n1 > n2:
    print('O primeiro é maior que o segundo, o número é {:.2f} .'.format(n1))
if n1 < n2:
    print('O segundo é maior que o primeiro, o número é {:.2f} .'.format(n2))
if n1 == n2:
    print('Os dois números são iguais.')

