"""
Faça um programa que calcule o número médio de alunos por turma.
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma.
As turmas não podem ter mais de 40 alunos.
"""

q_turma = int(input('Informe a quantidade de Turmas:\n'))
while q_turma <= 0:
    print('A turma não pode ter valor 0 pois senão não existiria.\nTente novamente.')
    q_turma = int(input())
a = 1
c = 1
lista1 = []
lista = []
for c in range(1, q_turma + 1):
    q_alunos = int(input('Informe a quantidade de alunos da {}° turma:\n'.format(a)))
    while q_alunos <= 0 or q_alunos > 40:
        print('A quantidade de alunos não pode ser 0 e nem maior que 40.Tente novamente. ')
        q_alunos = int(input())
    lista1.append(c)  # Quantidade de turmas
    lista.append(q_alunos)  # Quantidade de alunos
    a += 1
    c += 1
media = sum(lista) / len(lista1)
print('A média de alunos por turma e de {:.2f}.'.format(media))

