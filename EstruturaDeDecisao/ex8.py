"""
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo
que a decisão é sempre pelo mais barato.
"""
p1 = float(input('Informe o preço do produto 1:\n'))
p2 = float(input('Informe o preço do produto 2:\n'))
p3 = float(input('Informe o preço do produto 3:\n'))

if p1 <= p2 <= p3:
    print(20 * '=')
    print('Você deverá levar o produto 1.')
    print(20 * '=')

if p1 <= p3 <= p2:
    print(40 * '=')
    print('Você deverá levar o produto 1.')
    print(40 * '=')

if p2 <= p3 <= p1:
    print(40 * '=')
    print('Você deverá levar o produto 2.')
    print(40 * '=')

if p2 <= p1 <= p3:
    print(40 * '=')
    print('Você deverá levar o produto 2.')
    print(40 * '=')

if p3 <= p2 <= p1:
    print(40 * '=')
    print('Você deverá levar o produto 3.')
    print(40 * '=')

if p3 <= p1 <= p2:
    print(40 * '=')
    print('Você deverá levar o produto 3.')
    print(40 * '=')

input()

