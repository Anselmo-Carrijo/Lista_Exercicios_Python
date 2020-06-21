"""
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por
aluno e apresentar:
A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
A mensagem "Reprovado", se a média for menor do que sete;
A mensagem "Aprovado com Distinção", se a média for igual a dez
"""
n1 = float(input('Digite a Primeira nota:\n'))
n2 = float(input('Digite a Segunda nota:\n'))

media = (n1 + n2) / 2

if 7 <= media <= 9:
    print('Você foi aprovado.Parabéns')
elif media < 7:
    print('Que pena! Você foi reprovado.')
else:
    print('Aprovado com Distinçao.Parabéns.')
input('Digite algo para sair.')
    
