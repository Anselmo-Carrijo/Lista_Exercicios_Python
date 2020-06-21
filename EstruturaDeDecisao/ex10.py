"""
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
"""

t = input('informe o seu turno de estudo.(M- Matutino, V- Vespertino ou N- Noturno)\n').__str__().capitalize().strip()

if t == 'M':
    print('Bom dia!')

elif t == 'V':
    print('Boa tarde!')

elif t == 'N':
    print('Boa noite!')

else:
    print('Valor inválido, tente novamente.')

input()
