"""
Faça um Programa que peça as quatro notas de 10 alunos,
calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.

"""
alunos = [[], [], [], [], []]

a = 1
for c in range(1, 5):
    nota = float(input('Informe a {}° nota do {}° aluno.\n'.format(c, a)))
    while 0 > nota or nota > 10:
        print('Informe notas entre 0 e 10 somente...')
        print('Informe novamente a {}° nota do {}° aluno.'.format(c, a))
        nota = float(input())
    alunos[0].append(nota)
    media1 = sum(alunos[0]) / 4
    if c == 4:
        a += 1
print('===' * 10)

for c in range(1, 5):
    nota = float(input('Informe a {}° nota do {}° aluno.\n'.format(c, a)))
    while 0 > nota or nota > 10:
        print('Informe notas entre 0 e 10 somente...')
        print('Informe novamente a {}° nota do {}° aluno.'.format(c, a))
        nota = float(input())
    alunos[1].append(nota)
    media2 = sum(alunos[1]) / 4
    if c == 4:
        a += 1
print('===' * 10)

for c in range(1, 5):
    nota = float(input('Informe a {}° nota do {}° aluno.\n'.format(c, a)))
    while 0 > nota or nota > 10:
        print('Informe notas entre 0 e 10 somente...')
        print('Informe novamente a {}° nota do {}° aluno.'.format(c, a))
        nota = float(input())
    alunos[2].append(nota)
    media3 = sum(alunos[2]) / 4
    if c == 4:
        a += 1
print('===' * 10)

for c in range(1, 5):
    nota = float(input('Informe a {}° nota do {}° aluno.\n'.format(c, a)))
    while 0 > nota or nota > 10:
        print('Informe notas entre 0 e 10 somente...')
        print('Informe novamente a {}° nota do {}° aluno.'.format(c, a))
        nota = float(input())
    alunos[3].append(nota)
    media4 = sum(alunos[3]) / 4
    if c == 4:
        a += 1
print('===' * 10)

for c in range(1, 5):
    nota = float(input('Informe a {}° nota do {}° aluno.\n'.format(c, a)))
    while 0 > nota or nota > 10:
        print('Informe notas entre 0 e 10 somente...')
        print('Informe novamente a {}° nota do {}° aluno.'.format(c, a))
        nota = float(input())
    alunos[4].append(nota)
    media5 = sum(alunos[4]) / 4
    if c == 4:
        a += 1
print('=====' * 10)

media = [media1, media2, media3, media4, media5]
quantidade_alunos = []
for c in media:
    if c >= 7:
        quantidade_alunos.append(c)
print('As médias foram {}.'.format(media))
print('Teve {} alunos acima da média (7 pontos).'.format(len(quantidade_alunos)))
print('=====' * 10)

