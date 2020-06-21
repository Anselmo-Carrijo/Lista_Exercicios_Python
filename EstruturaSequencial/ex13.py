"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7

"""
h = float(input('Digite a sua altura:\n'))

ph = (72.7 * h) - 58
pm = (62.1 * h) - 44.7

print('O peso ideal para homem é {:.2f} e mulher é {:.2f} Kilos. '.format(ph, pm))

