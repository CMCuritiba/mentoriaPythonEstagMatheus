"""
Loop for

Loop -> EStrutura de repetição
For -> Uma dessas estruras
C ou Java

For(int i = 0; i < 10; i++)
{
//execução do loop
}

Python

for item in interavel:
//execução do loop

utilizamos loops for interar sobre sequência ou sobre valores iteráveis

Exemplos de iteráveis:
- String
    nome = 'Geek University'
- Lista
    lista = [1, 3, 5, 7, 9]
- Range
    numer = range(1, 10)
"""

"""
nome = 'Matheus'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

# Exemplo de for 1
for letra in nome:
    print(letra)

# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)

# Exemplo de for 3 (Iterando sobre um range)
range(valor_inicial, valor_final)

obs: O valor final não é inclusive.
1
2
3
4
5
6
7
8
9
10 - não

for numero in range(1, 10):
    print(numero)
    
enumerate:
((0, 'M'), (1, 'a'), (2, 't'))

for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):
    print(letra)

Obs: Quando não precisamos de um valor, podemos descartá-lo utilizando um underline(_)

nome = 'Matheus'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) # Temos que transformar em uma lista

for valor in enumerate(nome):
    print(valor)
    
Outra forma de utilização do for:
qtd = int(input('Quantas vezes esse loop deve rodas ?'))
soma = 0

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:  '))
    soma = soma + num
print(f'A soma é {soma}')

Declarar caracteres sem pular linha:
nome = 'Matheus'
for letra in nome:
    print(letra, end='')

"""



