"""
Faça um programa que mostre os n termos da Série a seguir:
  S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m.
Imprima no final a soma da série.

"""
n = int(input("Digite o valor de n: "))
numerador = denominador = 1
S = 0

for i in range(1, n + 1):
    print("Termo {}: {}/{}".format(i, numerador, denominador))
    S += (numerador/denominador)
    numerador += 1
    denominador += 2

print("Soma total: {:.2f}".format(S))