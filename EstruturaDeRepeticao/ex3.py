"""
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';

"""
print(100 * '|==|')
nome = input('Informe um nome:\n')
while len(nome) <= 3:
    nome = input('Informe um nome com mais de 3 Letras.\n')
print(100 * '|==|')

idade = int(input("Informar idade entre 0 e 150 ."))
while idade > 150 or idade < 0:
    idade = int(input("Informar idade entre 0 e 150 ."))
print(100 * '|==|')

salario = int(input('Informe o salário:\n'))
while salario < 0:
    salario = int(input('Informe um salário maior que 0.\n'))
print(100 * '|==|') 

sexo = input('Digite F para Feminino ou M para masculino:\n').__str__().upper().strip()
while sexo != 'F' and sexo != 'M':
    sexo = input('Digite F para Feminino ou M para masculino:\n')
print(100 * '|==|')

civil = str(input("informe o seu estado civil:\n"
                  "1 - Casado\n"
                  "2 - Solteiro\n"
                  "3 - Divorciado\n"
                  "4 - Viuvo"))
while civil != "1" and civil != "2" and civil != "3" and civil != "4":
    civil = str(input("Informe o seu estado civil corretamente:\n"
                      "1 - Casado\n"
                      "2 - Solteiro\n"
                      "3 - Divorciado\n"
                      "4 - Viuvo\n"))
print(100 * '|==|')

print('Fim...')

