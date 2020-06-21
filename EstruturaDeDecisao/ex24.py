"""
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar.
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
A : par ou ímpar;
B : positivo ou negativo;
C:  inteiro ou decimal.
"""
n = float(input('Insira o primeiro número:\n'))
n1 = float(input('Insira o segundo número:\n'))
print(50 * '=')
print('Qual operação deseja fazer? \n'
      '1 - Adição\n'
      '2 - Subtrção\n'
      '3 - Multiplicação\n'
      '4 - exponenciação\n')
print(50 * '=')

operacao = input('Escolha opção: ')

if operacao != '1' or '2' or '3' or '4':
    print('Escolha inválida.Escolha somente:\n'
          ' 1, 2, 3 ou 4')
    exit()

print(50 * '=')

if operacao == '1':
    resultado = n + n1
    print('Você escolheu a adição. Soma = ({}) .'.format(resultado))
    if resultado % 2 == 0:
        a = 'Par'
    else:
        a = 'Ímpar'

    if resultado < 0:
        b = 'Negativo'
    else:
        b = 'Positivo'

    if resultado // 1 == resultado:
        c = 'Inteiro'
    else:
        c = 'Decimal'

    print('O número digitado é {},{} e {} .'.format(a, b, c))

    print(50 * '=')

if operacao == '2':
    resultado = n - n1
    print('Você escolheu a Subtração. Subtração = ({}) .'.format(resultado))

    if resultado % 2 == 0:
        a = 'Par'
    else:
        a = 'Ímpar'

    if resultado < 0:
        b = 'Negativo'
    else:
        b = 'Positivo'

    if resultado // 1 == resultado:
        c = 'Inteiro'
    else:
        c = 'Decimal'

    print('O número digitado é {},{} e {} .'.format(a, b, c))

    print(50 * '=')

if operacao == '3':
    resultado = n * n1
    print('Você escolheu a Multiplicação.Resultado = ({}) .'.format(resultado))

    if resultado % 2 == 0:
        a = 'Par'
    else:
        a = 'Ímpar'

    if resultado < 0:
        b = 'Negativo'
    else:
        b = 'Positivo'

    if resultado // 1 == resultado:
        c = 'Inteiro'
    else:
        c = 'Decimal'

    print('O número digitado é {},{} e {} .'.format(a, b, c))

    print(50 * '=')

if operacao == '4':
    resultado = n ** n1
    print('Você escolheu a Exponenciação.Resultado = ({}) .'.format(resultado))

    if resultado % 2 == 0:
        a = 'Par'
    else:
        a = 'Ímpar'

    if resultado < 0:
        b = 'Negativo'
    else:
        b = 'Positivo'

    if resultado // 1 == resultado:
        c = 'Inteiro'
    else:
        c = 'Decimal'

    print('O número digitado é {},{} e {} .'.format(a, b, c))

    print(50 * '=')

input('Digite algo para sair...')
