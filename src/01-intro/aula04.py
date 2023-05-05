
# Variáveis são containers para armazenar dados
# Python realiza a inferência de tipo, que significa que o programador não precisa indicar o tipo da variável

numero = 31 # Não é necessário declarar o tipo, como "int numero = 31"
print(numero, type(numero))

numero = 20 # É possível alterar o valor de uma variável durante o código

nome, idade, estado = "Maria", 60, "São Paulo" # Multiplas variáveis sendo declaradas em uma linha
print(nome, idade, estado)


a = b = c = 10 # Múltiplas variáveis recebendo o mesmo valor
print(a, b, c)

b = 20
print(a, b, c) # A mudança do valor de uma das variáveis não altera as outras



# Constantes são containers que não alteram seu valor
# Declaradas em LETRAS MAIÚSCULAS

ACELERACAO_GRAVIDADE = 10
PI = 3.14
RESPOSTA = 42
print(ACELERACAO_GRAVIDADE, PI, RESPOSTA)



# Literais são valores não associados a variáveis ou constantes

print("AAAAAAAAA", 123321) # Literais sendo exibidos



# Valores numéricos

idade = 18 # INTEGER
altura = 1.72 # FLOAT
print(idade, type(idade))
print(altura, type(altura))



# Strings: Cadeias de texto
# Declarados com aspas simples ou duplas

nome = "Guilherme"
teste = 'aaaaaaaaaaa'
print(nome, type(nome))



# Booleanos

print(True, type(True))
print(False, type(False))



# None
print(None, type(None))



# Coleções: Lista, Tupla, Conjunto, Dicionario

lista = [1, 2, 3] # (list) Mutável
print(lista, type(lista))

tupla = (3, 2, 1) # (tuple) Imutável
print(tupla, type(tupla))

conjunto = {"a", "b", "c", "a", "b"} # (set) Não permite elementos duplicados e não possui ordem específica de elementos
print(conjunto, type(conjunto))

dicionario = {"chave": "valor", "chave_2": "valor 2"} # (dictionary) Esquema de chave-valor
print(dicionario, type(dicionario))