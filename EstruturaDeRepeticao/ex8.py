"""
Faça um programa que leia 5 números e informe a soma e a média dos números.

"""
lista = []
b = 0
"""for a in range(0, 5):
    b += 1
    lista.append(int(input('Digite o {}° Número\n:'.format(b))))
media = sum(lista) / len(lista)
print('A soma dos {} números é {} e a média é {} .'.format(b, sum(lista), media))"""

a = 1
while a <= 5:
    a += 1
    b += 1
    lista.append(int(input('Digite o {}° Número\n:'.format(b))))
media = sum(lista) / len(lista)
print('A soma dos {} números é {} e a média é {} .'.format(b, sum(lista), media))
