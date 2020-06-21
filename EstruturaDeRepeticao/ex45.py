"""
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao
aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a
nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno
vai utilizar o sistema. Após todos os alunos terem respondido informar:

A - Maior e Menor Acerto;
B - Total de Alunos que utilizaram o sistema
C - A Média das Notas da Turma

Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

"""

c = 0
pontos = 0
for c in range(1, 11):
    resposta = str(input('Informe a {}° resposta.'.format(c)))
    if c == 1 and resposta == 'a':
        pontos += 1
    if c == 2 and resposta == 'b':
        pontos += 1
    if c == 3 and resposta == 'c':
        pontos += 1
    if c == 4 and resposta == 'd':
        pontos += 1
    if c == 5 and resposta == 'e':
        pontos += 1
    if c == 6 and resposta == 'e':
        pontos += 1
    if c == 7 and resposta == 'd':
        pontos += 1
    if c == 8 and resposta == 'c':
        pontos += 1
    if c == 9 and resposta == 'b':
        pontos += 1
    if c == 10 and resposta == 'a':
        pontos += 1

    else:
        pontos = pontos
        c += 1
print('Você acertou {} questões.'.format(pontos))
