"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos,
cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
"""
a = list()
b = list()
inter = list()

c = 0
while c != 10:
    n = int(input('Informe o {}° número do Vetor A.\n'.format(c + 1)))
    print('====' * 10)
    a.append(n)
    c += 1

c = 0
while c != 10:
    n = int(input('Informe o {}° número do Vetor B.\n'.format(c + 1)))
    print('======' * 10)
    b.append(n)
    c += 1

c = 0
while c != 10:
    inter.append(a[c])
    inter.append(b[c])
    c += 1

print(f'A primeira lista é {a}')
print('======='*10)
print(f'A Segunda  lista é {b}')
print('========='*10)
print(f'A lista intercalada é {inter}')
print('========='*10)
