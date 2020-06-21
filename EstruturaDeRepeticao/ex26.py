"""
Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores.
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

"""
total_eleitores = int(input('Informe a quatidade de eleitores habilitados:\n'))

while total_eleitores <= 0:
    print('Erro!\nA quantidade de eleitores tem que ser maior que 0. Tente novamente.')
    total_eleitores = int(input())

lista_votos = []
for c in range(1, total_eleitores + 1):
    total_votos = int(input('Informe seu voto:\n'
                            '1-Lula\n'
                            '2-Bolsonaro\n'
                            '3-Marina\n'))
    while total_votos < 1 or total_votos > 3:
        print('Informe um candidato válido:\n'
              '1-Lula\n'
              '2-Bolsonaro\n'
              '3-Marina')
        total_votos = int(input())

    lista_votos.append(total_votos)
cd1 = lista_votos.count(1)
cd2 = lista_votos.count(2)
cd3 = lista_votos.count(3)

print('Nesta eleição Lula recebeu {} votos, Bolsonaro recebeu {} votos e Marina recebeu {} votos.'.format(cd1, cd2, cd3))
if max(cd1, cd2, cd3) == cd1:

        print('O vencedor das eleições foi Lula com {} votos.'.format(max(cd1, cd2, cd3)))
elif max(cd1, cd2, cd3) == cd2:

        print('O vencedor das eleições foi Bolsonaro com {} votos.'.format(max(cd1, cd2, cd3)))
else:
        print('O vencedor das eleições foi Marina com {} votos.'.format(max(cd1, cd2, cd3)))










