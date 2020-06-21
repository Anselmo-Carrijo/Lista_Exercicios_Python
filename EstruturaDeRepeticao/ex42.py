"""
Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100].
A entrada de dados deverá terminar quando for lido um número negativo.

"""
def l():
    print(20 * '===')

numeros_0_25 = []
numeros_26_50 = []
numeros_51_75 = []
numeros_76_100 = []

print('Informe a quantidade de números que deseja testar.\n'
      'Lembrando que tem que estar no intervalo de  0 a 100 somente.')
l()
c = 0
a = 1
while c >= 0:
    q_num = int(input('Digite o {}° Número.\n'.format(a)))
    l()
    while 0 <= q_num > 100:
        print('Informe somente números entre 0 e 100.')
        q_num = int(input())
        l()
    c += 1
    a += 1
    if 0 <= q_num <= 25:
        numeros_0_25.append(q_num)
    elif 26 <= q_num <= 50:
        numeros_26_50.append(q_num)
    elif 51 <= q_num <= 75:
        numeros_51_75.append(q_num)
    elif 76 <= q_num <= 100:
        numeros_76_100.append(q_num)
    if q_num < 0:
        print('Verificando a quantidade de números fornecidos {},\n {} estão entre '
              '0-25,\n {} estão entre 26-50,\n {} estão entre 51-75,\n {} estão entre '
              '76-100 .'.format(c, len(numeros_0_25), len(numeros_26_50), len(numeros_51_75), len(numeros_76_100)))
        c = -1
        l()
