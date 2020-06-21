"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a
menor e a maior temperaturas informadas, bem como a média das temperaturas.

"""
n_temp = int(input('Informe a quantidade de temperaturas que deseja cadastrar:\n'))
temperaturas = []
a = 1
for c in range(1, n_temp + 1):
    print(('Informe a {}°temperatura:'.format(a)))
    temp = float(input())
    temperaturas.append(temp)
    c += 1
    a += 1
print('A menor temperatura é: {:.1f}° Celsius.'.format(min(temperaturas)))
print('A maior temperatura é: {:.1f}° Celsius.'.format(max(temperaturas)))
print('A media temperatura é: {:.1f}° Celsius.'.format(sum(temperaturas) / len(temperaturas)))













