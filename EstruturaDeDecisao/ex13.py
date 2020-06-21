"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""
n = input('Digite um número entre (1 e 7):\n ')

if n not in ('1','2','3','4','5','6','7'):
    print('Digite um valor válido.')
if n == '1':
    print('Hoje é Domingo.')
if n == '2':
    print('Hoje é Segunda.')
if n == '3':
    print('Hoje é Terça-Feira.')
if n == '4':
    print('Hoje é Quarta-Feira.')
if n == '5':
    print('Hoje é Quinta-Feira.')
if n == '6':
    print('Hoje é Sexta-Feira.')
if n == '7':
    print('Hoje é Sabado.')
input()

