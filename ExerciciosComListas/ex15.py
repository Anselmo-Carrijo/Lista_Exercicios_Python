"""
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, encerrando a entrada de dados quando
for informado um valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
A: Mostre a quantidade de valores que foram lidos;
B : Exiba todos os valores na ordem em que foram informados, um ao lado do outro;
C : Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro;
D : Calcule e mostre a soma dos valores;
E : Calcule e mostre a média dos valores;
F : Calcule e mostre a quantidade de valores acima da média calculada;
G : Calcule e mostre a quantidade de valores abaixo de sete;
H : Encerre o programa com uma mensagem;

"""
from time import sleep
c = -1
valores = []
q = []
b = []

while c != 0:
    print('Informe os valores...')
    v = float(input())

    if v < 0:
        print('====' * 10)

        # A: Mostre a quantidade de valores que foram lidos;
        print(f'Foram lidos {len(valores)} valores.')

        # B : Exiba todos os valores na ordem em que foram informados, um ao lado do outro
        print(f'A ordem em que foram informados são:{valores}')

        # C : Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro
        print('A ordem inversa um abaixo do outro:')
        valores.reverse()
        for z in range(0, len(valores)):
            print(valores[z])

        # D : Calcule e mostre a soma dos valores
        print(f'A soma dos valores é {sum(valores)}.')

        # E : Calcule e mostre a média dos valores;
        media = sum(valores) / len(valores)
        print('A média dos valores é {:.2f}'.format(media))

        # F : Calcule e mostre a quantidade de valores acima da média calculada
        for i in valores:
            if i > media:
                q.append(valores[valores.index(i)])
                c = len(q)
        print(f'O valores acima da média foi: {c}')

        # G : Calcule e mostre a quantidade de valores abaixo de sete

        for i in valores:
            if i < 7:
                b.append(i)
                b.reverse()

        print(f'Encontrado {len(b)} Números abaixo de 7. Segue os números: {len(b)}')
                         
        # H : Encerre o programa com uma mensagem
        print('======' * 10)
        print('Muito Obrigado por ter participado e interagido conosco.\n'
              'Saindo do programa em 3 Segundos...')
        sleep(3)
        print('======' * 10)
        print('FIM...')

        exit()
    valores.append(v)
    print('====' * 10)
