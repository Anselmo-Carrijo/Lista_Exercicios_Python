"""
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.

"""
a = []
b = []
d = []
inter = []
c = 0
while c != 2:
    n = int(input('Informe o {}° número do Vetor A.\n'.format(c + 1)))
    a.append(n)
    print('====' * 10)
    c += 1

c = 0
while c != 2:
    n = int(input('Informe o {}° número do Vetor B.\n'.format(c + 1)))
    b.append(n)
    print('======' * 10)
    c += 1

c = 0
while c != 2:
    n = int(input('Informe o {}° número do Vetor C.\n'.format(c + 1)))
    d.append(n)
    print('======' * 10)
    c += 1

c = 0
while c != 2:
    inter.append(a[c])
    inter.append(b[c])
    inter.append(d[c])
    c += 1

print(f'A primeira lista é {a}')
print('=======' * 10)
print(f'A Segunda  lista é {b}')
print('=========' * 10)
print(f'A Terceira  lista é {d}')
print('=========' * 10)
print(f'A lista intercalada é {inter}')
print('=========' * 10)

