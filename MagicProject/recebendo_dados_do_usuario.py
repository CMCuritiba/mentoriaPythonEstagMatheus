"""
Recebendo dados do usuário

input() -> todo dado recebido via input é do tipo String

Em Python tudo o que estiver entre:
 - Aspas simples;
 - Aspas duplas;
 - Aspas simples triplas;
 - Aspas duplas triplas;

 Exemplos:
 - Aspas simples -> 'Angelina Jolie'
 - Aspas duplas -> "Angelina"
 - Aspas simples triplas -> '''Angelina'''
 """
 # - Aspas duplas triplas -> """Angelina"""

# Entrada de dados
# print("Qual é seu nome ?")
# nome = input()
# Exemplo de print 'antigo' 2.x
# print('Seja bem-vindo(a) %s\n' % nome)

nome = input('Qual seu nome ?\n')

# Exemplo de print 'moderno' 3.x
# print('Seja bem-vindo(a) {0}'.format(nome))

# Exemplo de print 'mais atual' 3.7
print(f'Seja bem-vindo(a) {nome}')

print('Qual a sua idade ?')
idade = input()

# Processamento

# Saída
# Exemplo de print 'antigo' 2.x

# Exemplo de print 'moderno' 3.x
# print('{0} tem {1} anos'.format(nome, idade))

# Exemplo de print 'mais atual' 3.7
print(f'{nome} tem {idade} anos')

"""
# int(idade) => cast

Cast é a 'Conversão' de um tipo de dado para outro
"""

print(f'{nome} nasceu em {2020 - int(idade)}')
