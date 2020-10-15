"""
Estruturas lógicas and, not, or, is
Operadores unários:
    - not
Operadores binários:
    - and, or, is

Regras de funcionamento:
Para o 'and', ambos os valores precisam ser True'
Para o 'or', um ou outro valor precisa ser True
Para o 'not', o valor do booleano é invertido, ou seja, se for True, vira False, se for False vira True
"""
ativo = True""""""
logado = True
"""
if ativo and logado:
    print('Usuário ativo no sistema')
else:
    print('Você precisa ativar sua conta, Por favor, cheque seu e-mail')
"""

"""
# Se não estiver ativo:
if not ativo:
    print('Você precisa ativar sua conta. Cheque seu email!!')
else:
    print('Bem-vindo usuário')
"""


if logado is ativo:
    print('Você precisa ativar sua conta. Cheque seu email')
else:
    print('Bem-vindo usuário')

print(not False)

