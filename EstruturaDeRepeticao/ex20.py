"""
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o
fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

"""
cont = 0

quant = int(input('informe a quantidade de vezes de deseja fazer o calculo de fatoração:\n'))

while quant != cont:

    numero = int(input('Digite um número inteiro:\n'))

    while numero > 16:
        print('Digite números inteiros de 1 a 16 somente...')
        numero = int(input())
    c = numero
    f = 1
    print('O fatorial de {}! = '.format(numero), end='')
    while c > 0:
        print('{}'.format(c), end='')
        print(' x ' if c > 1 else ' = ',end='')
        f *= c
        c -= 1
    cont += 1
    print('{}'.format(f))

