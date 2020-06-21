"""
Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00,
receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e
a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente.

"""
fruta = int(input('Informe a fruta.\n1 - Morangos 2 - Maçãs\n'))

if 1 != fruta != 2:
    print('Informe um valor válido: (1 ou 2)')
    exit()

if fruta == 1:
    fruta1 = 'Morango'
else:
    fruta1 = 'Maçãs'

if 1 == fruta == 2:
    print('Digite 1 - Morangos e 2 - Maçãs')
    exit()
kg_q = float(input('Forneça a quantidade em Kg:\n'))

if fruta == 1:
    kg = 2.5
    kg1 = 2.2
    if kg_q <= 5:
        valor = kg_q * kg
        valor_total = valor
    if 5 < kg_q <= 8:
        valor = kg_q * kg1
        valor_total = valor
    if kg_q > 8 or valor_total > 25:
        valor = kg_q * kg1
        valor_total = valor - (10 / 100 * valor)

if fruta == 2:
    kg = 1.8
    kg1 = 1.5
    if kg_q <= 5:
        valor = kg_q * kg
        valor_total = valor
    if 5 < kg_q <= 8:
        valor = kg_q * kg1
        valor_total = valor
    if kg_q > 8 or valor_total > 25:
        valor = kg_q * kg1
        valor_total = valor - (10 / 100 * valor)

print('Você comprou {:.2f} Kg de {}, valor total é de R$ {:.2f} reais.'.format(kg_q, fruta1, valor_total))
