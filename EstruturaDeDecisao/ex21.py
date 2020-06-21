"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar
quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais.
O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas
existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50,
uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50,
quatro notas de 10, uma nota de 5 e quatro notas de 1.

"""
saque = int(input('Quanto deseja sacar?\n'
                  'Obs: Mínimo R$ 10,00 e Máximo R$ 600,00\n'))

if saque < 10 or saque > 600:
    print('Digite um valor de saque válido. de R$ 10,00 até R$ 600,00 Reais')
    exit()

nota100 = saque // 100  # Quantidade notas de 100
nota_100 = saque % 100  # Restante das notas de 100

nota50 = nota_100 // 50  # Quantidade notas de 50
nota_50 = nota_100 % 50  # Quantidade notas de 50

nota10 = nota_50 // 10  # Quantidade notas de 10
nota_10 = nota_50 % 10  # Quantidade notas de 10

nota5 = nota_10 // 5  # Quantidade notas de 5
nota_5 = nota_10 % 5  # Restante notas de 5

nota1 = nota_5 // 1  # Quantidade notas de 1
nota_1 = nota_5 % 1  # Restante notas de 1

print('Você vai receber:')

if nota100 // 100 == 0:
    print('{} notas de R$ 100'.format(nota100))

if nota50 // 50 == 0:
    print('{} notas de R$ 50'.format(nota50))

if nota10 // 10 == 0:
    print('{} notas de R$ 10'.format(nota10))

if nota5 // 5 == 0:
    print('{} notas de R$ 5'.format(nota5))

if nota_1 // 1 == 0:
    print('{} notas de R$ 1'.format(nota1))





