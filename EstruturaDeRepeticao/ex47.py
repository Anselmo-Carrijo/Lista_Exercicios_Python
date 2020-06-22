"""
Em uma competição de ginástica, cada atleta recebe votos de sete jurados.
A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes.
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados alcançadas pelo
atleta em sua apresentação e depois informe a sua média, conforme a descrição acima informada
(retirar o melhor e o pior salto e depois calcular a média com as notas restantes). As notas não são informados ordenadas.
Um exemplo de saída do programa deve ser conforme o exemplo abaixo:
Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04

"""
nome = str(input('Informe o nome do atleta:\n'))
notas = []

c = 1
for n in range(1, 8):
    nota = float(input('Informe a nota do {}° Jurado.'.format(c)))
    notas.append(nota)
    maximo = max(notas)
    minimo = min(notas)
    c += 1
print('===' * 10)

print('Nome atleta: {}'.format(nome))
c = 1
for n in notas:
    print('Nota do {}° jurado: {}'.format(c, n))
    c += 1

maximo = max(notas)
minimo = min(notas)
notas.remove(maximo)
notas.remove(minimo)

media = sum(notas) / len(notas)
print('===' * 10)
print('Resultado Final:')
print('Atleta: {}'.format(nome))
print('Melhor nota: {}'.format(maximo))
print('Pior nota: {}'.format(minimo))
print('Média: {}'.format(media))
print('===' * 10)

