"""
Exercícios 06 do curso da Udemy;

Fazer um programa para receber dois números, e verificar qual é o maior e a diferença entre eles
"""
print('Digite o primeiro número')
num1 = int(input())

print('Digite o segundo número')
num2 = int(input())

if num1 > num2:
    print(f'o número {num1} é maior que {num2}')
    print(f'A diferença entre eles é {num1 - num2}')
elif num1 == num2:
    print('Os número são iguais...')
else:
    print(f'o número {num2} é maior que {num1}')
    print(f'A diferença entre eles é {num2 - num1}')
