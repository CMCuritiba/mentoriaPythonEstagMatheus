"""
Exercícios 04 do curso da Udemy;

Fazer um programa para receber um número, se for positivo calcular e mostra o número ao quadrado e a raiz dele;
"""
import math

print('Digite um número para realizar as contas...')
num = int(input())

print(f'O {num} ao quadrado é {num * num} e sua raiz é {math.sqrt(num)}')
