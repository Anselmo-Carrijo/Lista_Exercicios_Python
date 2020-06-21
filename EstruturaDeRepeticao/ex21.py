"""
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
Um número primo é aquele que é divisível somente por ele mesmo e por 1.

"""

n = int(input('Digite um número , vou informar se e um número primo.'))
tot = 0
for c in range(1, n + 1):
    if n % c == 0:
        tot += 1
        c += 1
if tot == 2:
    print('O número {} é Primo.'.format(n))
else:
    print('O número {} não é Primo.'.format(n))



