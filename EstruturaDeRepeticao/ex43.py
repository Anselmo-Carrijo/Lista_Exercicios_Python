"""
O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas.
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do pedido.
Considere que o cliente deve informar quando o pedido deve ser encerrado.

"""
print('====' * 10)
print("Especificação   Código  Preço")

print("Cachorro Quente 100     R$ 1,20")

print("Bauru Simples   101     R$ 1,30")

print("Bauru com ovo   102     R$ 1,50")

print("Hambúrguer      103     R$ 1,20")

print("Cheeseburguer   104     R$ 1,30")

print("Refrigerante    105     R$ 1,00\n")
print('====' * 10)

valor = 0
soma = 0
i = 1
codigo = 1
produto_l = ['Cachorro Quente', 'Bauru Simples', 'Bauru com ovo', 'Hambúrguer', 'Cheeseburguer', 'Refrigerante']
while codigo != 0:
    codigo = int(input('Digite o codigo do produto ou 0 para sair --->\n '))
    if codigo != 0:
        qty = int(input('Digite a quantidade do produto ---> '))

        if codigo == 100:
            valor = 1.2
            produto = produto_l[0]

        elif codigo == 101:
            valor = 1.3
            produto = produto_l[1]

        elif codigo == 102:
            valor = 1.5
            produto = produto_l[2]

        elif codigo == 103:
            valor = 1.2
            produto = produto_l[3]

        elif codigo == 104:
            valor = 1.3
            produto = produto_l[4]

        elif codigo == 105:
            valor = 1.0
            produto = produto_l[5]

        valorParcial = valor * qty
        print(codigo, ' -- ', qty, produto, ' --- R$', round(valorParcial, 2))
        soma = soma + valorParcial
if soma != 0:
    print('Valor total ---> R$ {:.2f} Reais.'.format(soma))
