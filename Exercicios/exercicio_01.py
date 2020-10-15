"""
Exercícios 01 do curso da Udemy;

Fazer um programa para receber dois números e mostrar qual é o maior;
"""

print('Digite o primeiro número')
num1 = input()

print('Digite o segundo número')
num2 = input()

if num1 > num2:
    print(f'o número {num1} é maior que {num2}')
elif num1 == num2:
    print('Os número são iguais...')
else:
    print(f'o número {num2} é maior que {num1}')
