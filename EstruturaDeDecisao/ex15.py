"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar se os valores podem ser um triângulo.
Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
"""
l1 = float(input('Digite o valor do 1° lado do triângulo:\n'))
l2 = float(input('Digite o valor do 2° lado do triângulo:\n'))
l3 = float(input('Digite o valor do 3° lado do triângulo:\n'))

if l1 + l2 <= l3 or l1 + l3 <= l2 or l2 + l3 <= l1:
    print('Essas medidas não são válidas para montar um triângulo.')

elif l1 == l2 == l3:
    print('Equilatero')
elif l1 == l2 or l1 == l3 or l2 == l3:
    print('Isósceles')
else:
    print('Escaleno.')

input()
