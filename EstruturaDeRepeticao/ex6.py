"""
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro.
Depois modifique o programa para que ele mostre os números um ao lado do outro.

"""
a = 0
while a <= 19:
    a += 1
    print(a)

for a in range(1, 21):
    print(a, '', end='')
