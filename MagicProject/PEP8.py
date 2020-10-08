"""
PEP8 - Python Enhancement Proposal
São propostas de melhorias para linguagem Python, escrever python de forma bonita
Zen of Python
Import this
[1] - Utilize Camel Case para nomes de classes
class Calculadora:
    pass


class CalculadoraCientifica:
    pass

[2] - Utilize Nomes em minúsculo, separados por underline para funções
def soma():
    pass


def soma_dois():
    pass

numero = 4

numero_impar = 5

[3] - Utilize 4 espaços para identação!!(importante)
if'a' in 'banana':
    print('tem')

[4] - Linhas em branco
- Separar funções e definições de classe em duas linhas em branco;
- Método dentro de uma classe devem ser separados com uma única linha em branco;
class Classe:
    pass

class Outra:
    pass
[5] - Imports
- Imports devem ser sempre feitos em linhas separadas;
# Import Errado

import sys, os

# Import Certo

import sys
import os

# Não há problemas em utilizar:

from types import StringType, ListType

# Caso tenha muitos improts de uma mesmo pacote, recomenda-se fazer:

from types import (
    StringType,
    ListType,
    SetType,
    OutroType
)

# Imports devem ser colocados no topo do arquivo, logo depois de quaisquer comentários ou docstrings e
# antes de cosntantres ou variáveis globais.

[6] - Espaços em expressões e instruções
# Não faça:

funcao( algo[ 1 ], { outro: 2 })

# Faça:

funcao(algo[1], {outro: 2})

# Não faça:

algo (1)

# Faça:

algo(1)

# Não Faça:

dict ['chave'] = list [indice]

# Faça:

dict['chave'] = lista[indice]

# Não Faça:

x              = 1
y              = 3
variavel_longa = 5

# Faça:

x = 1
y = 3
variavel_longa = 5

[7] - Termine sempre uma instrução com uma nova linha

"""