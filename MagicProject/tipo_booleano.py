"""
Tipo Booleano

álgebra Booleana, criada por George Boole

2 constantes, verdadeiro ou falso

True -> Verdadeiro
False -> Falso

Obs: sempre com inícial maiúscula

Errado:

true, false

Certo:

True, False


"""

ativo = False

print(ativo)

"""
Operação básicas:
"""

# Negação (not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso,
se for falso o  resultado será verdadeiro. oU SEJA, SEMPRE AO CONTRÁRIA.
"""
print(not ativo)

logado = False

# Ou (or);

"""
É uma operação binária, ou seja, depende de dois valores. ou um ou outro deve ser verdadeiro.

True or True -> True
True or False -> True
False or True -> True
False or False -> False
"""

print(ativo or logado)

# E (and)

"""
Também é uma operação ninária, ou seja, depende de dois valores. Ambos os valores devem ser verdadeiros.

True and True -> True
True or False -> False
False or True -> False
False or False -> False
"""


