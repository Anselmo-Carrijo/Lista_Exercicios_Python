"""
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário,
mostrando uma mensagem de erro e voltando a pedir as informações.

"""
nome = input('Digite o seu usuário:\n')
senha = input('Digite a sua senha:\n')

while nome == senha:
    print('A sua senha não pode ser igual ao seu nome.Tente novamente.')
    nome = input('Digite o seu usuário:\n')
    senha = input('Digite a sua senha:\n')

print('Cadastro efetuado com sucesso...')
