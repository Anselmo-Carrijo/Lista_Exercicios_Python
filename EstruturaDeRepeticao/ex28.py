"""
Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor
médio gasto em cada um deles.
O usuário deverá informar a quantidade de CDs e o valor para em cada um.
"""
q_cd = int(input('Informe a quantidade de CD´s:\n'))
while q_cd <= 0:
    print('Erro!!!\n'
          'A quantidade de cds tem que ser maior que 0.Tente novamente.')
    q_cd = int(input())
lista_cd = []
valor_cd = []
a = 1
c =1
for c in range(0, q_cd):
    print('Informe o valor do {}° CD.'.format(a))
    valor = float(input())
    lista_cd.append(c)
    valor_cd.append(valor)
    a += 1
    c += 1
valor_medio = sum(valor_cd) / len(lista_cd)
print('O valor médio gasto e de R$ {:.2f} Reais.'.format(valor_medio))

