# Tipos de dados


# Valores numéricos

idade = 20 # INTEGER
altura = 1.85 # FLOAT
print(idade, type(idade))
print(altura, type(altura))



# Strings

nome = "Guilherme"
sobrenome = 'Macedo'
nome_sobrenome = nome + " " + sobrenome # Junção (concatenação) de duas variáveis do tipo string
print(nome_sobrenome)

produto = "banco"


print(f"O cliente {nome} {sobrenome} comprou o produto {produto}") # Interpolação de strings

print(nome[0], nome[1], nome[2], nome[-1]) # Selecionando letras específicas de dentro de strings

print(nome.upper()) # Strings possuem métodos que ajudam a utilizá-las

print(1, 2, 3, 4, sep=" --- ") # O separador de valores normal na função print é um " " mas é possível substituir



# Booleanos

resultado = 10 < 3 # Pode ser retornado a partir de uma operação
resultado2 = True # Ou declarado diretamente
print(resultado)
print(resultado2)



# Listas

frutas = ["banana", "maçã", "laranja"]
print(frutas[0], frutas[1], frutas[2], sep=", ") # Também é possível selecionar elementos específicos em listas

frutas[0] = "uva" # Os valores são mutáveis
frutas.append("Pêra") # É possível adicionar valores na lista também
print(frutas)
print(len(frutas))

for fruta in frutas:
    print(fruta.upper()) # Por meio de loops é possível passar por todos os valores em uma lista



# Tupla

codigo = (11, 22, 33)
print(codigo[0]) # Também é possível selecionar elementos específicos
print(len(codigo)) # Ou achar o seu tamanho

#codigo[0] = 12321 # Mas não modificar elementos



# Conjunto

sorteio = {10, 55, 22, 9, 5} # Multiplos elementos únicos
print(sorteio)

sorteio.add(13) # É possível adicionar novos elementos em um conjunto
print(sorteio)



# Dicionário

funcionarios = {
    1: "Rodrigo",
    2: "Ricardo",
    3: "Rogério"
}


print(funcionarios)
print(funcionarios[1]) # É possível selecionar valores específicos a partir da chave
print(funcionarios[2])
print(funcionarios[3])

print(funcionarios.keys()) # É possível retirar todas as chaves de um dicionário
print(funcionarios.values()) # Ou apenas os seus valores

funcionarios[1] = "Ronaldo" # Ou substituir valores
print(funcionarios)

