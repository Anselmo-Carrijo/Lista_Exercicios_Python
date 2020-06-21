"""
Altere o programa anterior para mostrar no final a soma dos números.

"""
lista = []
a = 0
n = 0
for a in range(0, 2):
    a += 1
    n += 1
    lista.append(int(input('Digite o {}° Número:\n'.format(n))))
b = lista[0]
c = lista[1]
soma = sum(lista)

if lista[0] - lista[1] == 1 or lista[1] - lista[0] == 1:
    print('Não possui números intermediários.')
    print('A soma dos números é {}.'.format(soma))

else:
    print('Os números intermediários são:')
    while c > (b + 1):
        b += 1
        print(b, end=' || ')
    print()
    print('A soma dos números é {}.'.format(soma))
