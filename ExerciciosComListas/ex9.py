"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.

"""

a = []
c = 0
while c != 10:
    n = int(input('Informe {}° numero:'.format(c + 1)))
    aux = n**2
    a.append(aux)
    c += 1
print('==='*10)
print('A soma dos quadrados é: {}'.format(sum(a)))







