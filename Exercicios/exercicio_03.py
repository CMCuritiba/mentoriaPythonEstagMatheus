"""
Exercícios 03 do curso da Udemy;

Fazer um programa para receber um número, se for positivo fazer a raiz, se for negativo ele ao quadrado;
"""
import math

print('Digite um número....')
num = int(input())

if num >= 0:
    print(f'A raiz de {math.sqrt(num)} é ')
elif num < 0:
    print(f'O número {num} elevado ao quadrado é {num * num}')
