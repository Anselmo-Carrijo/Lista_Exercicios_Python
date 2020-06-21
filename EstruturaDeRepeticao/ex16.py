"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120

"""
numero = int(input('Digite um número inteiro:\n'))
c = numero
f = 1
print('O fatorial de {}! = '.format(numero), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ',end='')
    f *= c
    c -= 1
print('{}'.format(f))

numero = int(input('Digite um número inteiro:\n'))
print('O fatorial de {}! = '.format(numero), end='')
c = 0
f = 1
for c in range(numero, 0, -1):
    print(c, end='', )
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print('{}'.format(f))
