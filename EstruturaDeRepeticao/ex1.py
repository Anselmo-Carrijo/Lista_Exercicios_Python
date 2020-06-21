"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

"""
nota = float(input('Informe um número entre 0 e 10.\n'))
while nota < 0 or nota > 10:
    nota = float(input(('Número válido, Tente novamente.\n')))
else:
    print('Valor válido.Prossiga')
