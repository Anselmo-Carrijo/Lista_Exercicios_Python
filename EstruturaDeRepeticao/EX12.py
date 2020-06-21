"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro entre 1 a 10.
O usuário deve informar de qual numero ele deseja ver a tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50

"""

n = int(input('Informe qual tabuada deseja.(De 1 a 10 .)\n'))
d = 0
while n <= 0 or n > 10:
    d += 1
    print('informe um número válido.(De 1 a 10.)')
    n = int(input())
else:
    c = 0
    print(15 * '=')
    for b in range(0, 9):
        c += 1
        print('||',n, 'x', c, '=', n * c,'||')
print(15 * '=')

