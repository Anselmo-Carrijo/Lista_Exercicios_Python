"""
Altere o programa de cálculo dos números primos,
informando, caso o número não seja primo, por quais número ele é divisível.

"""

n = int(input('Digite um número , vou informar se e um número primo.'))
tot = []
for c in range(1, n + 1):
    if n % c == 0:
        tot.append(c)
        c += 1
if tot == 2:
    print('O número {} é Primo.'.format(n))
else:
    print('O número {} não é Primo.'.format(n))
print('Ele é dividido pelos números:{}'.format(tot))

