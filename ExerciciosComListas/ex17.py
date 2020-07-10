"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus
saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando não for
informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m

"""

saltos = []

nome = str(input('Informe o nome do atleta:\n'))

for i in range(1, 6):
    distancia = float(input(f'informe o {i}° Salto.'))
    saltos.append(distancia)

print('Resultado Final:')
print(f'Atleta : {nome}')

a = 0
for i in range(1, 6):
    print(f'{i}° Salto: {saltos[a]} Metros.')
    a += 1
media = sum(saltos) / len(saltos)
print(f'A média dos saltos é de {media} Metros.')
