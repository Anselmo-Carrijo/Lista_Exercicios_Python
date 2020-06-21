"""
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e
agora possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora rudimentar.
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra. O programa deve então mostrar o
total da compra e perguntar o valor em dinheiro que o cliente forneceu, para então calcular e mostrar o valor do troco.
Após esta operação, o programa deverá voltar ao ponto inicial, para registrar a próxima compra.
A saída deve ser conforme o exemplo abaixo:
Lojas Tabajara
Produto 1: R$ 2.20
Produto 2: R$ 5.80
Produto 3: R$ 0
Total: R$ 9.00
Dinheiro: R$ 20.00
Troco: R$ 11.00
...
"""


def linha():
    print(7 * '=========')


def inicio():
    listap = []
    a = 1
    preco = 1
    print('Nova compra...')
    linha()

    while preco != 0:
        preco = float(input('Informe o preço do {}° produto ou Digite 0 para finalizar compra:\n'.format(a)))
        linha()
        if preco < 0:
            print('Não existe compra com valor negativo.Favor Informe novamente o preço.')
            preco = float(input('Informe o preço do {}° produto ou Digite 0 para finalizar compra:\n'.format(a)))
        listap.append(preco)
        a += 1
        valorc = sum(listap)
    print('O valor da compra é de R$ {:.2f} Reais.'.format(valorc))
    linha()
    dinheiro = float(input('Quanto vai pagar em dinheiro:\n'))
    linha()
    troco = dinheiro - valorc
    print('O seu troco é de R$ {:.2f} Reais.\n'        
          'Obrigado pela compra.'.format(troco))

    linha()
    linha()
    saida = int(input('Deseja fechar o caixa?\n'
                  '1- Sim\n'
                  '2- não\n'))
    linha()
    if saida == 1:
        print('O caixa será fechado....')
        linha()
        exit()
    else:
        inicio()
        while inicio != 0:
            inicio()

inicio()

