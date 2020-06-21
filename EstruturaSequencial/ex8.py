# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas
# no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor = float(input('Quanto você recebe por hora?'))
if valor <=0:
    print('Favor digite um valor válido.')
    exit()

horas_trabalhadas = float(input('Digite a quantidade de horas trabalhadas no mês.'))

if horas_trabalhadas <=0:
    print('Favor digite um valor válido.')
    exit()

pagamento = valor * horas_trabalhadas

print('O valor do seu pagamento no mês e de : {} Reais.'.format(pagamento))


