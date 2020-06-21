"""
Faça um Programa que peça um número inteiro e determine se ele é par ou impar.
Dica: utilize o operador módulo (resto da divisão).

"""
n = int(float(input('Digite um número, vou dizer se é par ou impar:\n')))
if n % 2 == 0:
    print('O número é par.')
else:
    print('O número é impar.')