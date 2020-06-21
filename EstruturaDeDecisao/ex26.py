"""
Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
A : até 20 litros, desconto de 3% por litro
B : acima de 20 litros, desconto de 5% por litro
Gasolina:
A : até 20 litros, desconto de 4% por litro
B : acima de 20 litros, desconto de 6% por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de
combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente
sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.

"""
litros = float(input('Digite a quantidade de litros:\n'))
print('Qual combustível? G (Gasolina) A (Álcool)')
tipo = str.upper(input()).strip()

if tipo != 'G' and tipo != 'A':
    print('Informe somente G - (Gasolina) ou A - (Álcool)')
    exit()
if tipo == 'A':
    valor_fixo = 1.9
    if litros <= 20:
        valor_real = (valor_fixo * litros) - (valor_fixo * litros) * (3 / 100)
        print('Você abasteceu {:.2f} litros de álcool.Valor é de R$ {:.2f} Reais.'.format(litros, valor_real))
    if litros > 20:
        valor_real = (valor_fixo * litros) - (valor_fixo * litros) * (5 / 100)
        print('Você abasteceu {:.2f} litros de álcool.Valor é de R$ {:.2f} Reais.'.format(litros, valor_real))

if tipo == 'G':
    valor_fixo = 2.5
    if litros <= 20:
        valor_real = (valor_fixo * litros) - (valor_fixo * litros) * (4 / 100)
        print('Você abasteceu {:.2f} litros de gasolina.Valor é de R$ {:.2f} Reais.'.format(litros, valor_real))
    if litros > 20:
        valor_real = (valor_fixo * litros) - (valor_fixo * litros) * (6 / 100)
        print('Você abasteceu {:.2f} litros de gasolina.Valor é de R$ {:.2f} Reais.'.format(litros, valor_real))
input('Digite algo para sair...')












