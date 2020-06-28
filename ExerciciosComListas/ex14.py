"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
A : "Telefonou para a vítima?"
B : "Esteve no local do crime?"
C: "Mora perto da vítima?"
D: "Devia para a vítima?"
E : "Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

"""
respostas = list()

print('Telefonou para a vítima?')
print('S - Sim\n'
      'N - Não')
r = str(input()).upper()
while r != 'S' and r != 'N':
    print('Informe somente S - Sim ou N - Não...')
    r = str(input()).upper()
else:
    respostas.append(r)

print('Esteve no local do crime?')
print('S - Sim\n'
          'N - Não')
r = str(input()).upper()
while r != 'S' and r != 'N':
    print('Informe somente S - Sim ou N - Não...')
    r = str(input()).upper()
else:
    respostas.append(r)

print('Mora perto da vítima?')
print('S - Sim\n'
          'N - Não')
r = str(input()).upper()
while r != 'S' and r != 'N':
    print('Informe somente S - Sim ou N - Não...')
    r = str(input()).upper()
else:
    respostas.append(r)

print('Devia para a vítima?')
print('S - Sim\n'
          'N - Não')
r = str(input()).upper()
while r != 'S' and r != 'N':
    print('Informe somente S - Sim ou N - Não...')
    r = str(input()).upper()
else:
    respostas.append(r)

print('Já trabalhou com a vítima?')
print('S - Sim\n'
          'N - Não')
r = str(input()).upper()
while r != 'S' and r != 'N':
    print('Informe somente S - Sim ou N - Não...')
    r = str(input()).upper()
else:
    respostas.append(r)
sim = respostas.count('S')

if sim == 2:
    print('Você é uma pessoa suspeita...')
elif 3 <= sim <= 4:
    print('Você é cumplice do assasinato...')
elif sim >= 5:
    print('Você é o Assassino.')
else:
    print('Você é Inocente...')
