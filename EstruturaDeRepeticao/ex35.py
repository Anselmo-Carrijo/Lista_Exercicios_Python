"""
Encontrar números primos é uma tarefa difícil.
Faça um programa que gera uma lista dos números primos existentes
entre 1 e um número inteiro informado pelo usuário.

"""
num = int(input('Informe um número:\n'))
lista = []
lista1 = []
for c in range(1, num + 1):
    lista.append(c)
    if num % c == 0:
        lista1.append(len(lista))
        c += 1

print('Lista completa: {}\n'
      'Os primos são : {}'.format(lista,lista1))