"""
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

"""
lista = []
count = 0

n = int(input("Digite a quantiade de número que deseja digitar : "))
while n <= 0:
    print('(Não pode ser 0 e nem Menor que 0:)...')
    n = float(input("Digite um número Válido: "))
while n != count:
    numero = float(input("Digite um número: "))
    while numero > 1000 or numero < 0:
        numero = float(input("Digite um número[erro]: "))

    lista.append(numero)
    count += 1
print("Lista: ", lista, "\nMaior: ", max(lista), "\nMenor: ", min(lista))
print("Soma: ", max(lista) + min(lista))






