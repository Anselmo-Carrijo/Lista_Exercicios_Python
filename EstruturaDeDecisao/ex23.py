"""
Faça um Programa que peça um número e informe se o número é inteiro ou decimal.
Dica: utilize uma função de arredondamento.
"""
n = float(input('Digite um número:\n'))

if (round(n) / n) == 1:
    print('Inteiro')
else:
    print('Decimal')


