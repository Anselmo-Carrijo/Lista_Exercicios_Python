"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a
média de idade da turma varia entre 0 e 25, 26 e 60 e maior que 60; e então, dizer se a turma é jovem,
adulta ou idosa, conforme a média calculada.
"""
qp = float(input('Informe a quantidade de pessoas no grupo:\n'))

while qp <= 0:
    qp = float(input('ERRO!!!\nInforme número maior que 0:\n'))
qp = int(qp)
idade = []
a = 1
for c in range(0, qp):
    idade.append(int(input('Idade da {}° Pessoa:\n'.format(a))))
    c += 1
    a += 1

    media = sum(idade) / len(idade)

if media <= 25:
    print('Este grupo é jovem.')
elif media <= 60:
    print('Este grupo é adulto.')
elif media > 60:
    print('Este grupo é Idoso.')


