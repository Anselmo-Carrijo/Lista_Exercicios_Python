"""

Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados: valor da dívida, valor dos juros,
quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67

"""
import os

def l():
    print(15 * '===')


l()
divida = float(input('Informe o valor da dívida:\n'))
l()
parcelas = int(input('Informe a quantidade de parcelas:\n'
                     '1 , 3 , 6 , 9 ou 12 vezes.\n'))
l()
l_parcelas = (0, 2, 4, 5, 7, 8, 10, 11)

while parcelas in l_parcelas:
    parcelas = int(input('Informe a quantidade de parcelas:\n'
                         '1 , 3 , 6 , 9 ou 12 vezes.\n'))
    l()
if parcelas == 1:
    juros = divida
    a = 0
elif parcelas == 3:
    juros = divida * (1 / 10) + divida
    a = divida * ( 1 / 10)
elif parcelas == 6:
    juros = divida * (15 / 100) + divida
    a = divida * (15 / 100)
elif parcelas == 9:
    juros = divida * (20 / 100) + divida
    a = divida * (20 / 100)
else:
    juros = divida * (25 / 100) + divida
    a = divida * (25 / 100)



l_juros = [1, 3, 6, 9, 12]

while parcelas in l_juros:
    print('Você tem uma dívida de R$ {} Reais, juros de R$ {} Reais.Total a pagar é de  R$ {} Reais.'.format(divida, a , juros))
    print('Pressione algo para sair...')
    os.abort()


