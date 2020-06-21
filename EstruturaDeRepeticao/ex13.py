"""
Faça um programa que peça dois números, base e expoente, calcule e mostre
o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem.

"""
lista =[]
for a in range(0, 1):
    lista.append(float(input('Digite um Número Base.\n')))
for a in range(0, 1):
    lista.append(float(input('Digite um Número Expoente.\n')))
ex = lista[0] ** lista[1]
print('O valor da exponenciação é {:.2f}'.format(ex))
