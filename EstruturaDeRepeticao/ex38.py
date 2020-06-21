"""
Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
A: Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
B: Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
C: A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior.
Faça um programa que determine o salário atual desse funcionário.
Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário.

"""
def programa():

     from datetime import date

     print(20 * '===')

     salario_inicial = float(input(('Informe o seu salário inicial:\n')))
     salario_inicial = (salario_inicial * (1.5 / 100)) + salario_inicial
     ano_inicio = int(input('Informe o ano que iniciou:\n'))

     data = date.today()

     salario_atual = []
     for c in range(ano_inicio, data.year):
          salario_atual.append(salario_inicial)
          salario_inicial = (salario_inicial * (3 / 100)) + salario_inicial

     print('O salário atual do funcionário é de R$ {:.2f} Reais.'.format(max(salario_atual)))


     return(programa())

programa()







