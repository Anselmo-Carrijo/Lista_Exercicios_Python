"""
Foram anotadas as idades e alturas de 30 alunos.
Faça um Programa que determine quantos alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos.

"""


idades = list()
alturas = list()
i = 0
soma = 0

# Obtendo os valores dos vetores
c = 1
while c != 5:
    idade = int(input(f'Informe a idade do {c}° aluno.\n'))
    idades.append(idade)
    altura = float(input(f'Informe a altura do {c}° aluno.\n'))
    alturas.append(altura)
    c += 1
# Obtendo a média
while i < len(alturas):
    soma += alturas[i]
    i += 1
media = soma / len(alturas)

# obtendo a quantidade de alunos
c = 0
quantidade = 0
while c < len(idades):
    if idades[c] > 13 and alturas[c] < media:
        quantidade += 1
    c += 1
print(quantidade)





