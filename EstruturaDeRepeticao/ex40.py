"""
Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito.
Foram obtidos os seguintes dados:
A: Código da cidade;
B: Número de veículos de passeio (em 1999);
C: Número de acidentes de trânsito com vítimas (em 1999).

Deseja-se saber:
A: Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
B: Qual a média de veículos nas cinco cidades juntas;
C: Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio.
"""


def linha():
    print(15 * '===')


cod_cidade = []
num_veiculos = []
num_acidentes = []

for c in range(1, 6):
    linha()
    cidade = int(input('Informe o código da cidade:\n'))
    while cidade <= 0:
        print('Digite um código maior que 1:')
        cidade = int(input())
    while cidade in cod_cidade:
        linha()
        print('Cidade já cadastrada.Informe outro código.')
        cidade = int(input())

    linha()
    veiculos = int(input('Informe a quantidade de veículos em 1999:\n'))
    acidentes = int(input('Informe a quantidade de acidentes em 1999:\n'))

    cod_cidade.append(cidade)
    num_veiculos.append(veiculos)
    num_acidentes.append(acidentes)

media_veiculos = (sum(num_veiculos) / len(cod_cidade))

maior_acidente = max(num_acidentes)
cidade_maior_acidente = (cod_cidade[num_acidentes.index(max(num_acidentes))])

menor_acidente = min(num_acidentes)
cidade_menor_acidente = (cod_cidade[num_acidentes.index(min(num_acidentes))])


def l():
    print(40 * '==')


l()
l()
print('o maior  índice de acidentes de transito e {} a cidade tem código: {}'.format(maior_acidente,
                                                                                     cidade_maior_acidente))
print('o menor  índice de acidentes de transito e {} a cidade tem código: {}'.format(menor_acidente,
                                                                                     cidade_menor_acidente))
print('A média de veículos das {} cidades é {}:'.format(c, media_veiculos))
l()
l()
