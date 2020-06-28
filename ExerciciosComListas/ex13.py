"""
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma lista. Após isto, calcule
a média anual das temperaturas e mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).

"""
temperatura = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro',
         'Novembro', 'Dezembro']

c = 1
while c != 13:
    if c == 1:
        m = 'Janeiro'
    elif c == 2:
        m = 'Fevereiro'
    elif c == 3:
        m = 'Março'
    elif c == 4:
        m = 'Abril'
    elif c == 5:
        m = 'Maio'
    elif c == 6:
        m = 'Junho'
    elif c == 7:
        m = 'Julho'
    elif c == 8:
        m = 'Agosto'
    elif c == 9:
        m = 'Setembro'
    elif c == 10:
        m = 'Outubro'
    elif c == 11:
        m = 'Novembro'
    elif c == 12:
        m = 'Dezembro'

    mes = float(input(f'Informe a média do mês de {m}:\n'))
    print('====' * 10)
    temperatura.append(mes)
    c += 1
    media_anual = sum(temperatura) / len(temperatura)

for i in temperatura:
    if i > media_anual:
        mes = meses[temperatura.index(i)]
        print('===='*10)
        print(f'O mês de {mes} teve média de {i}.')

print('===='*10)



