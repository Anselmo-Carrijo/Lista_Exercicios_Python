"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o
mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve
fazer um programa que pergunte a cada um dos clientes da academia seu código,
sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código.
Ao encerrar o programa também deve ser informados os códigos e valores do cliente mais alto, do mais baixo,
do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes

"""
cod_l = []
alt_l = []
peso_l =[]
c = 1
def linhas():
    print(70 * '=')
while c != 0:
    cod = int(input('Informe o seu código:\n'))
    linhas()
    if cod == 0:
        print('Os códigos dos clientes são: {}'.format(cod_l))
        linhas()
        print('O cliente mais alto tem {:.2f} metros e o mais baixo tem {:.2f} metros.'.format(max(alt_l), min(alt_l)))
        linhas()
        print('O cliente mais pesado tem {:.2f} Kilos e o mais magro tem {:.2f} Kilos.'.format(max(peso_l), min(peso_l)))
        linhas()
        print('A média dos pesos é {:.2f} Kilos.'.format(sum(peso_l) / len(peso_l)))
        linhas()
        print('A média das alturas é {:.2f} metros.'.format(sum(alt_l) / len(alt_l)))
        linhas()
        exit()

    alt = float(input('Informe a sua altura:\n'))
    linhas()
    peso = float(input('Infome o seu peso:\n'))
    linhas()

    cod_l.append(cod)
    alt_l.append(alt)
    peso_l.append(peso)

