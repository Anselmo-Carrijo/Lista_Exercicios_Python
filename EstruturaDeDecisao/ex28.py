"""
O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                 Acima de 5 Kg             Até 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg

Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção,
porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente
receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade
de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade
de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.
"""

print('Escolha a sua promoção Tabajaras:\n'
      '1 - Filé Duplo\n'
      '2 - Alcatra\n'
      '3 - Picanha')
promocao = int(input())

# Identifica o Produto
if promocao == 1:
    a = 'Filé Duplo'
elif promocao == 2:
    a = 'Alcatra'
else:
    a = 'Picanha'


# opçoes produtos válidos
if promocao != 1 and promocao != 2 and promocao != 3:
    print('Informe somente os números da promoção. 1, 2 ou 3. ')
    exit()
# quantidade de Kg
print('Informe a quantidade em Kg de {}.'.format(a))
kg = float(input())

# Produto 1
if promocao == 1:
    if kg < 5 :
        valor_total = kg * 5.8
    if kg > 5 :
        valor_total = kg * 4.9
    desconto = (0.05 * valor_total)

# Produto 2
if promocao == 2:
    if kg < 5 :
        valor_total = kg * 6.8
    if kg > 5 :
        valor_total = kg * 5.9
    desconto = (0.05 * valor_total)

# Produto 3

if promocao == 3:
    if kg < 5 :
        valor_total = kg * 7.8
    if kg > 5 :
        valor_total = kg * 6.9
    desconto = (0.05 * valor_total)

pagamento = int(input('Informe a forma de pagamento:\n'
                          '1 - Dinheiro:\n'
                          '2 - Cartão Tabajaras:\n'))
if pagamento == 1:
    b = 'Dinheiro'
    desconto = 0
if pagamento == 2:
    b = 'Cartão Tabajaras'
    desconto = (0.05 * valor_total)
valor_total = valor_total - desconto

print(40 * '=','Cupom Fiscal', 40 * '=')
print('O tipo de carne é {}.\n'
      'A quantidade é de {:.2f} kilos.\n'
      'O tipo de pagamento foi {}.\n'
      'O valor do desconto é de R$ {:.2f} reais.\n'
      'O valor a pagar é de R$ {:.2f} reais.'.format(a, kg, b, desconto, valor_total ))
print(94 * '=')













