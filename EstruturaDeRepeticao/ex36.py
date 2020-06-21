"""
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário,
mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser
informados também pelo usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
Obs: Você deve verificar se o usuário não digitou o final menor que o inicial.

"""
tabuada = int(input('Informe qual tabuada deseja montar:\n'))
while tabuada < 1 or tabuada > 10:
    print('Você tem que informar números de 1 a 10 somente..')
    tabuada = int(input())

comecar = int(input('Quer começar por qual número?\n'))
terminar = int(input('Deseja terminar por qual número?\n'))

while terminar < comecar:
    terminar = int(input('ERRO!!! Por favor informe novamente um número maior que começar...\n'))

for c in range(comecar, terminar + 1):
    print(tabuada, 'x', comecar, '=', (tabuada*comecar))
    comecar += 1


