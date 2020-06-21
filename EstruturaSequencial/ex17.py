"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da
tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou
em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o preço seja o menor. Acrescente 10% de folga e sempre arredonde os valores para
cima, isto é, considere latas cheias.

"""
from math import ceil

metros = float(input('Digite o tamanho da área em metros:\n'))
litros = (1 / 6) * metros
latasg = ceil(litros / 18)
valorg = latasg * 80

litrosp = (1 / 6) * metros
latasp = ceil(litros / 3.5)
valorp = latasp * 25


print('Você vai precisar de {:.2f} lata de tinta (18L),com valor total de {:.2f} Reais.'.format(latasg, valorg))
print('Ou também tem a escolha de {:.2f} lata de tinta (3.5L), com valor total de {:.2f} Reais.'.format(latasp, valorp))

if valorp <= valorg:
    print(90 * '=')
    print('Neste casso aconselhamos você levar a tinta mais barata (3.5L) no valor de {:.2f} Reais.'.format(valorp))
    print(90 * '=')
else:
    print(90 * '=')
    print('Neste casso aconselhamos você levar a tinta mais barata (18L) no valor de {:.2f} Reais.'.format(valorg))
    print(90 * '=')




