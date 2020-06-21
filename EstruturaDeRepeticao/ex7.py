"""
Faça um programa que leia 5 números e informe o maior número.
"""
lista = []
b = 0
print('Digite 5 números, irei informar o maior deles:\n')
for a in range(0, 5):
    b += 1
    lista.append(int(input('Número {}:\n'.format(b))))
print('O maior número dos {} fornecidos é o {}.'.format(b, max(lista)))



