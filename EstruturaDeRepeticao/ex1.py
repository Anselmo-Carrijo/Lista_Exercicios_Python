"""
Faça um programa que peça uma nota, entre zero e dez.
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

"""
nota = float(input('Informe um número entre 0 e 10.\n'))
while 0 < nota > 10:
    nota = float(input(('Número Inválido, Tente novamente.\n')))
else:
    print('Valor válido.Prossiga')
