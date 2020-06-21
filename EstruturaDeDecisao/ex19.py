"""
Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do
mesmo.
Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
326 = 3 centenas, 2 dezenas e 6 unidades
12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16

"""

n = int(input(('Digite um número inteiro positivo entre 0 e 1000:\n')))

# Condições números válidos
if n <= 000 or n >= 1000:
    print('Digite um número válido')
    exit()

c = n // 100  # Quantidade de Centenas
c1 = n % 100  # Restante das Centenas
d = c1 // 10  # Quantidade de Dezenas
d1 = c1 % 10  # Restante das Dezenas
u = d1        # Quantidade de Unidades

if d // 10 == 1:
    print('Este número tem {} unidades'.format(u))
elif c // 100 == 1:
    print('Este número tem {} dezenas e {} unidades'.format(d, u))
else:
    print('Este número tem {} centenas, {} dezenas e {} unidades'.format(c, d, u))

