"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor.
Imprima a idade e a altura na ordem inversa a ordem lida.

"""
idade_l = []
alt_l = []
for c in range(1, 6):
    idade = float(input('Informe a idade da {}° Pessoa.\n'.format(c)))
    alt = float(input('Informe a Altura da {}° Pessoa.\n'.format(c)))
    print('====' * 10)
    idade_l.append(idade)
    idade_invertida = idade_l[::-1]
    alt_l.append(alt)
    alt_invertida = alt_l[::-1]


print('======='*10)
print('A ordem das idades foram {}.'.format(idade_l))
print('A ordem inversa das idades é {}'.format(idade_invertida))
print('A ordem das alturas foram {}.'.format(alt_l))
print('A ordem inversa das alturas é {}'.format(alt_invertida))
print('======='*10)

