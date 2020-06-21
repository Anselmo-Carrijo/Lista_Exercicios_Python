"""
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados.
"""
num = int(input('Informe um número inteiro:'))
div = []
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        div.append(c)
        c += 1
        tot += 1
if tot == 2:
    print('O número {}  é Primo e dividido pelos:{} , total de divisões: tot {}.'.format(num, div, tot))
else:
    print('O número {} não é primo e dividido pelos números:{}'.format(num, div))


