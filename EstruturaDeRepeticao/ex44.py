"""
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.

"""
voto = -1
soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
soma_nulo = 0
soma_branco = 0
nome1 = 'João'
nome2 = 'Maria'
nome3 = 'Lula'
nome4 = 'Ciro Gomes'
nome5 = 'Voto Nulo'
nome6 = 'Voto em Branco'

while voto != 0:
    voto = int(input('Informe o seu voto de 1 a 6 ou 0 para sair...\n'))
    print(10 * '==========')

    if voto != 0:
        if voto == 1:
            soma1 += 1

        elif voto == 2:
            soma2 += 1

        elif voto == 3:
            soma3 += 1

        elif voto == 4:
            soma4 += 1

        elif voto == 5:
            soma_nulo += 1

        elif voto == 6:
            soma_branco += 1
        total_votos = soma1 + soma2 + soma3 + soma4 + soma_nulo + soma_branco
        nulos_p = (soma_nulo * 100) / total_votos
        branco_p = (soma_branco * 100) / total_votos
print(nome1, 'recebeu', soma1, 'Votos,', nome2, 'Recebeu', soma2, 'Votos,', nome3, 'Recebeu', soma3, 'Votos', 'e', nome4,
      'Recebeu', soma4, 'Votos.')
print('Teve {} votos nulos e {} votos brancos.'.format(soma_nulo, soma_branco))

print('A porcentagem de votos nulos é de {:.2f}%.'.format(nulos_p))
print('A porcentagem de votos em brancos  é de {:.2f}%.'.format(branco_p))


print(10 * '==========')


