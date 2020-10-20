"""
Exercícios 07 do curso da Udemy;

Fazer um programa para receber duas notas, calcular a média se forém verdadeiras (de 0.0 a 10.0), se
 não forem verdareiras, imprimir na tela
"""
n1 = float(input('Digite a nota 1  '))
n2 = float(input('Digite a nota 2  '))

if n1 <= 10 and n1 >= 0 and n2 <= 10 and n2 >= 0:
    media = (n1 + n2) / 2
    print(f'A média é {media}')
else:
    print('Digite notas válidas...')
