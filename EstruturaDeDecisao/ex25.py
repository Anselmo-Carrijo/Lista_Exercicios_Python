"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
A : "Telefonou para a vítima?"
B : "Esteve no local do crime?"
C : "Mora perto da vítima?"
D : "Devia para a vítima?"
E : "Já trabalhou com a vítima?"

O programa deve no final emitir uma classificação sobre a participação da pessoa no crime.
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice"
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

"""
# pergunta 1

print('Vamos fazer algumas perguntas esperamos que responda com seriedade.Pois você pode ser preso.')
print("Telefonou para a vítima?")
print('1 - Sim\n'
      '2 - Não')
a = int(input())
if a != 1 and a != 2:
    print('Digite uma resposta válida...\n'
          'Tente novamente e não minta nas suas respostas.')
    exit()

print("Esteve no local do Crime?")
print('1 - Sim\n'
      '2 - Não')
b = int(input())
if b != 1 and b != 2:
    print('Digite uma resposta válida...\n'
          'Tente novamente e não minta nas suas respostas.')
    exit()

print("Mora perto da vítima?")
print('1 - Sim\n'
      '2 - Não')
c = int(input())
if c != 1 and c != 2:
    print('Digite uma resposta válida...\n'
          'Tente novamente e não minta nas suas respostas.')
    exit()

print("Devia para a vítima?")
print('1 - Sim\n'
      '2 - Não')
d = int(input())
if d != 1 and d != 2:
    print('Digite uma resposta válida...\n'
          'Tente novamente e não minta nas suas respostas.')
    exit()

print("já trabalhou com a vítima?")
print('1 - Sim\n'
      '2 - Não')
e = int(input())
if e != 1 and e != 2:
    print('Digite uma resposta válida...\n'
          'Tente novamente e não minta nas suas respostas.')
    exit()

lista = [a, b, c, d, e]
resposta = lista.count(1)



if resposta == 2:
    print('Suspeita')
elif 3 == resposta or resposta == 4:
    print('Cúmplice')
elif resposta == 5:
    print('Assassino. Você está preso.')
else:
    print('Você é inocente.')

print(lista)
print(resposta)

