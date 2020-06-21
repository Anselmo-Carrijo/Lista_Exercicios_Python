"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o
segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo.
Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

"""
def l():
    print(20 * '==')


codigo = []
centimetros = []
maior_alt = 0
for c in range(0, 10):
    codigo1 = round(float(input('Informe o Código do aluno:')), 0)
    int(codigo1)
    l()
    while codigo1 in codigo:
        print('Aluno ja cadastrado.Informe outro código...')
        codigo1 = round(float(input()), 0)
        int(codigo1)
        l()
        

    centimetros1 = float(input('Informe sua altura em centímetros:'))
    l()
    codigo.append(codigo1)
    centimetros.append(centimetros1)
maior_alt = max(centimetros) / 100
menor_alt = min(centimetros) / 100
a = (codigo[centimetros.index(max(centimetros))])
b = (codigo[centimetros.index(min(centimetros))])


print('O aluno mais alto tem {:.2f} metros e o seu código é: {}.'.format(maior_alt, a))
print('O aluno mais baixo tem {:.2f} metros e o seu código é: {}.'.format(menor_alt, b))
l()



























