"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na forma ax2 + bx + c.
O programa deverá pedir os valores de a, b e c e fazer as consistências, informando ao usuário nas seguintes situações:

a: Se o usuário informar o valor de A igual a zero, a equação não é do segundo grau e o programa não deve fazer pedir os
    demais valores, sendo encerrado;
b: Se o delta calculado for negativo, a equação não possui raizes reais. Informe ao usuário e encerre o programa;
c: Se o delta calculado for igual a zero a equação possui apenas uma raiz real; informe-a ao usuário;
d: Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário;

"""
from math import sqrt

a = int(input('Digite o coeficiente a da equação:\n'))
if a == 0:
    print('O coeficiente a não pode ser 0, pois deixa de ser uma equação do 2° grau.')
    exit()
else:
    b = int(input('Digite o coeficiente b da equação:\n'))
    c = int(input('Digite o coeficiente c da equação:\n'))

delta = (b ** 2) - (4 * a * c)  # Fórmula de Delta.


if delta < 0:
    print('Essa equação não possui raizes reais.')
    exit()

if delta == 0:
    x0 = -b / (2 * a) # calculo delta raiz zero
    print('Essa equação Possui somente uma raiz real {:.2f}.'.format(x0))
    exit()

# calculo das raizes
x = sqrt(delta)
x1 = (- b + x) / (2 * a)
x2 = (- b - x) / (2 * a)

if delta > 0:
    print('Essa equação possui 2 raizes, {:.2f} e {:.2f} .'.format(x1, x2))
    exit()






