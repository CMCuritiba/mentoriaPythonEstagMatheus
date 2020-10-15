"""
Exercícios 05 do curso da Udemy;

Fazer um programa para receber um número, e verificar se o mesmo é par ou ímpar
"""
print('Digite um número')
num = int(input())
if num % 2 == 0:
    print(f'{num} é par')
else:
    print(f'{num} é ímpar')
