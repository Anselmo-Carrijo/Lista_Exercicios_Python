"""
Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.

"""

v = []
i = 1
for c in range(0, 10):
    n = int(input('Informe {}° números real:\n'.format(i)))
    v.append(n)
    i += 1
print(v[::-1])
