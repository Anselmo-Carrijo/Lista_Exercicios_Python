"""
Faça um programa que receba dois números inteiros e gere os números inteiros
que estão no intervalo compreendido por eles.

"""

lista = []
a = 0
n = 0
for a in range(0, 2):
    a += 1
    n += 1
    lista.append(int(input('Digite o {}° Número:\n'.format(n))))

b = lista[0]
c = lista[1]

while c > (b + 1):
    b += 1

    print(b, '', end='')
