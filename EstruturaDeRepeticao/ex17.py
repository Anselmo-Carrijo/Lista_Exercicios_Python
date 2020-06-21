"""
Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.
"""
lista = []

print('Digite 5 números por favor:\n')
for c in range(0, 5):
    lista.append(int(input()))
lista.sort()
print('Os números digitados foram:', lista)
print('A soma de todos números é:', sum(lista))
print('O maior número é:', max(lista))
print('E o menor número é:', min(lista))


