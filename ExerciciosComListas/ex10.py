"""
Faça um Programa que leia dois vetores com 10 elementos cada.
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.

"""
a = []
b = []

c = 0
while c != 3:
    i = 0
    n = input('Informe um elemento para lista A:\n')
    a.append(n)
    c += 1
c = 0
while c != 3:
    i = 0
    n = input('Informe um elemento para lista B:\n')
    b.append(n)
    c += 1
