# Faça um Programa que calcule a área de um quadrado,
# em seguida mostre o dobro desta área para o usuário.

lado = float(input('Qual é o valor lado do quadrado em Metros?' ))

if lado <=0:
    print('Favor digite um valor válido.')
    exit()

area = (lado * lado) ** 2
print('O dobro da área do quadrado é: {} Metros.'.format(area))

