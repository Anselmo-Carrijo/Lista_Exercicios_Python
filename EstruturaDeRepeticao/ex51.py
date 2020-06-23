"""
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.

"""


n = int(input('Informe o denominador:\n'))
denominador = numerador = 1
s = 0
for i in range(n):
    i += 1
    print('Termo {} : {}/{}'.format(i, numerador, denominador))
    numerador += 1
    denominador += 2
    s += (numerador/denominador)
print('A soma dos termos é {:.2f}.'.format(s))




