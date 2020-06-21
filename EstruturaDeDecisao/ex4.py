"""
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letra = input('Digite uma letra e vou informar se é uma vogal ou não:\n ').__str__().capitalize()

vogal = ['A', 'E', 'I', 'O', 'U']

if letra in vogal:
    print('A letra digitada é a vogal {} .'.format(letra))
else:
    print('A letra digitada é a Consoante {} .'.format(letra))

