"""
Faça um Programa que leia três números e mostre-os em ordem decrescente.
"""
n1 = float(input('Digite o primeiro número:\n'))
n2 = float(input('Digite o segundo número:\n'))
n3 = float(input('Digite o terceiro número:\n'))

if n1 <= n2 <= n3:
    print(40 * '=')
    print('A orem decrescente é {}, {}, {} .'.format(n3, n2, n1))
    print(40 * '=')

if n1 <= n3 <= n2:
    print(40 * '=')
    print('A orem decrescente é {}, {}, {} .'.format(n2, n3, n1))
    print(40 * '=')

if n2 <= n3 <= n1:
    print(40 * '=')
    print('A orem decrescente é {}, {}, {} .'.format(n1, n3, n2))
    print(40 * '=')

if n2 <= n1 <= n3:
    print(40 * '=')
    print('A orem decrescente é {}, {}, {} .'.format(n3, n1, n2))
    print(40 * '=')

if n3 <= n1 <= n2:
    print(40 * '=')
    print('A orem decrescente é {}, {}, {} .'.format(n2, n1, n3))
    print(40 * '=')

if n3 <= n2 <= n1:
    print(40 * '=')
    print('A orem decrescente é {}, {}, {} .'.format(n1, n2, n3))
    print(40 * '=')

input()
