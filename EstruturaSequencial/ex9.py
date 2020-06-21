"""Faça um Programa que peça a temperatura em graus Farenheit, transforme e mostre a 
 temperatura em graus Celsius.
C = (5 * (F-32) / 9).
"""
F = float(input('Digite o valor da temperatura em Farenheit:'))
C = (5 * (F-32) / 9)
print('O valor convertido para celsius é {:.2f}°'.format(C))



