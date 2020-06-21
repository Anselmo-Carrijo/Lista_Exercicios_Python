"""
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda,
que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário
Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os
descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo.
No exemplo o valor da hora é 5 e a quantidade de hora é 220.
"""

horas = float(input('Informe quanto você recebe por hora em (R$):\n'))
horas_trabalhadas = float(input('Quantas horas você trabalhou este mês?\n'))

salario_bruto = horas * horas_trabalhadas
ir = salario_bruto * (5 / 100)
inss = salario_bruto * (10 / 100)
fgts = salario_bruto * (11 / 100)
total_descontos = (ir + inss)
salario_liquido = salario_bruto - total_descontos

print(200 * '=')
print('O salário bruto é de {} Reais.'.format(salario_bruto))
print('(-) Desconto IR (5%) é de {} Reais'.format(ir))
print('(-) Desconto INSS (10%) é de {} Reais'.format(inss))
print('FGTS (11%) no valor de {} Reais depositados pela empresa.'.format(fgts))
print('O total de descontos foi de {} Reais.'.format(total_descontos))
print('O salário liquido é de {} Reais.'.format(salario_liquido))
print(200 * '=')
input()











