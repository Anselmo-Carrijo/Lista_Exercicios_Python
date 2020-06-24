"""
Faça um Programa que leia 20 números inteiros e armazene-os num vetor.
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
"""
todos =[]
pares =[]
impares =[]
for c in range(1, 21):
    numero = int(input('Informe o {}° número:\n'.format(c)))
    todos.append(numero)
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)
print('Todos os numéros: {}'.format(todos))
print('Todos os pares: {}'.format(pares))
print('Todos os impares: {}'.format(impares))