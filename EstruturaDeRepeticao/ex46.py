"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados.
O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as
cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima
informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos.
Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for
informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m

"""
saltos = []
s = 1
print('Informe o seu nome:')
nome = str(input())

for s in range(1, 6):
    print('Informe o seu {}° Salto.'.format(s))
    salto = int(input())
    saltos.append(salto)
    s += 1
print('===' * 10)
print('Primeiro Salto:{}'.format(saltos[0]))
print('Segundo Salto:{}'.format(saltos[1]))
print('Terceiro Salto:{}'.format(saltos[2]))
print('Quarto Salto:{}'.format(saltos[3]))
print('Quinto Salto:{}'.format(saltos[4]))
print('=====' * 10)

saltos.sort()
ordem = saltos[1:4]
media = sum(ordem) / 3

print('Atleta: {}.'.format(nome))
print('Seu melhor salto foi de {:.2f} metros.'.format(max(saltos)))
print('Seu pior salto foi de {:.2f} metros.'.format(min(saltos)))
print('A média dos demais saltos foram {:.2f} metros.'.format(media))

print('Resultado Final atleta: {} : {:.2f} Metros.'.format(nome, media))

print('=====' * 10)
