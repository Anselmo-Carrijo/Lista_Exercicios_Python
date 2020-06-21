"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M".
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
letra = input('Digite uma letra:\n').__str__().capitalize()

if letra == 'F':
    print('O sexo é feminino.')
elif letra == 'M':
    print('O sexo é masculino.')
else:
    print('Algo deu errado!!! Digite somente F ou M')


