"""
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.

"""
n = []

for c in range(1, 6):
    n.append(c)
print(n)

print('====' * 10)

v = [c for c in range(1, 6)]
for x in v:
    print(x, end=' ')