"""
Exercício 02 do curso da Udemy;

Fazer um programa que cálcule a raiz se o número for positivo, e se for negativo dar mensagem de npumero inválido
"""
import math

num = int(input('Digite um número para o cálculo de raiz quadrada'))
raiz: int = math.sqrt(num)

if num >= 0:
    print(f'A raiz do {num} é {raiz}')
elif num < 0:
    print('Digite um número positivo')
