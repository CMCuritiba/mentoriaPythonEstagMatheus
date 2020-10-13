"""
em python, um dado é do tipo string sempre que:

-> Estiver entre aspas simples -> 'uma string', '234', 'm', 'True', '42,3'
-> Estiver entre aspas duplas -> "uma string", "234", "m", "True", "42,3"
-> Estiver entre aspas simples triplas -> '''uma string''', '''234''', '''m''', '''True''', '''42,3'''

nome = 'MagicGanza'
print(nome)
print(type(nome))

nome = "'Ginas's Bar"
print(nome)
print(type(nome))

print(nome.upper())

print(nome.lower())

print(nome.split()) # Transforma em uma lista de strings

nome = 'Matheus'
print(nome[0:4]) #Slice de string
"""
# -> Estiver entre aspas duplas triplas -> """uma string""", """234""", """a""", """True""", """42.3"""

texto= 'socorram me subino onibus em marrocos' #Palindromo
print(texto)

print(texto[::-1])








