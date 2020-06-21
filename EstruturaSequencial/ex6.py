# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = float(input('Digite o valor do raio do círculo em metros (M): '))

if raio <=0:
    print('Por favor digite um valor válido.Não existe medidas negativas e/ou nulas.')
    exit()

area = raio ** raio * 3.14
print('A área do círculo é {} Metros.'.format(area))





