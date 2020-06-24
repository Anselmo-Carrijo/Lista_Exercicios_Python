"""
Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
"""

notas = []

i = 1

for c in range(0, 4):
    numeros = int(input('Informe o {}° número.\n'.format(i)))
    notas.append(numeros)
    print('{}° número: {} '.format(i, numeros))
    print('==' * 10 + '======')
    i += 1
print('A média das notas é {:.2f}.'.format(sum(notas) / 4))
print('==' * 10 + '======')
