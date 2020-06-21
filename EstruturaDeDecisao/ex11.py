"""
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o
programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário
atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.

"""

salario = float(input('Digite o valor do seu salário:\n(R$): '))

faixa1 = salario + (20 / 100) * salario
faixa2 = salario + (15 / 100) * salario
faixa3 = salario + (10 / 100) * salario
faixa4 = salario + (5 / 100) * salario

if salario < 280:
    print('O seu salário antes do reajuste é de {} Reais.'
          '\nApós o reajuste passou a ser de {} reais.'.format(salario, faixa1))

if 280 <= salario <= 699:
    print('O seu salário antes do reajuste é de {} Reais.'
          '\nApós o reajuste passou a ser de {} reais.'.format(salario, faixa2))

if 700 <= salario <= 1499:
    print('O seu salário antes do reajuste é de {} Reais.'
          '\nApós o reajuste passou a ser de {} reais.'.format(salario, faixa3))

if salario >= 1500:
    print('O seu salário antes do reajuste é de {} Reais.'
          '\nApós o reajuste passou a ser de {} reais.'.format(salario, faixa4))

input()