"""
Os números primos possuem várias aplicações dentro da Computação, por exemplo na Criptografia.
Um número primo é aquele que é divisível apenas por um e por ele mesmo. Faça um programa que peça um
número inteiro e determine se ele é ou não um número primo.
"""

num = int(input('Informe um número:\n'))
divisores = []
for c in range(1, num + 1):
    if num % c == 0:
        divisores.append(c)
if len(divisores) > 2:
    print('O número {}, não é primo.\n'
          'O mesmo é dividido pelos números {}.'.format(num, divisores))
else:
    print('O número {}, é primo.\n'
          'O mesmo é dividido somente pelos números {}.'.format(num, divisores))

