"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.

"""
v = []
co = []
alf = [['A', 'E', 'I', 'O', 'U'],
       ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z']]
i = 1
for c in range(0, 10):
    print('Informe a {}° letra:'.format(i))
    letra = str(input()).upper()
    while letra not in alf[0] and letra not in alf[1]:
        print('Caracteres especiais e números não são válidos.\n'
              'Digite novamente...')
        letra = str(input('Informe a {}° letra\n'.format(i))).upper()
    if letra in alf[0]:
        v.append(letra)
    if letra in alf[1]:
        co.append(letra)
    i += 1
print('Você digitou {} Vogais e {} Consoantes.'.format(len(v), len(co)))

