"""
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais.
Valide a entrada e permita repetir a operação.

"""
a = float(input('Informe a população do Primeiro pais:\n'))
txa = float(input('Informe a taxa de crescimento do primeiro pais:\n'))
b = float(input('Informe a população do Segundo pais:\n'))
txb = float(input('Informe a taxa de crescimento do segundo pais:\n'))

txa = txa / 100
txb = txb / 100
ano = 0
while a <= b:
    ano = float(ano + 1)
    a = float(a + (a * txa))
    b = float(b + (b * txb))
while b <= a:
    ano = float(ano + 1)
    a = float(a + (a * txa))
    b = float(b + (b * txb))

print('Os países terao a mesma população em {} anos.'.format(ano))
