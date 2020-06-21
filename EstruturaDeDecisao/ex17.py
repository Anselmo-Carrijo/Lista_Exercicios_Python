"""
Faça um Programa que peça um número correspondente a um determinado ano e em
seguida informe se este ano é ou não bissexto.
"""

ano = int(input('Digite o ano para saber se ele é bissexto:\n'))

if ano % 100 != 0 and ano % 400 == 0 or ano % 4 == 0:
    print('O ano {} é Bissexto.'.format(ano))
else:
    print('O ano {} não é Bissexto.'.format(ano))
exit()

